import os
import requests
import shutil
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()

# === CONFIGURATION ===
OMDB_API_KEY = os.getenv("OMDB_API_KEY")
JELLYFIN_LIBRARY_PATH = "/Users/jonahmakowski/Desktop/GitHub/pyWrskp/src/jellyfinDownload/jellyfinMediaLibrary/"  # Replace with your Jellyfin library path
MOVIE_TITLE = "Sherlock Holmes"    # Replace with the desired movie title
MOVIE_YEAR = '1939'
MOVIE_TYPE = 'SHOW'

def search_movie(title, year=None):
    """Search for a movie using Internet Archive's API."""
    base_url = "https://archive.org/advancedsearch.php"
    params = {
        "q": f'title:"{title}" AND mediatype:movies' if year is None else f'title:"{title}" AND mediatype:movies AND year:{year}',
        "fl[]": "identifier,title,creator,year",
        "rows": 5,
        "output": "json"
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    if "response" in data and data["response"]["docs"]:
        return data["response"]["docs"]
    return None

def download_movie(identifier, dest_folder):
    """Download the best available movie file using metadata API with a progress bar."""
    base_url = f"https://archive.org/metadata/{identifier}"
    response = requests.get(base_url)
    response.raise_for_status()
    metadata = response.json()
    
    mp4 = False

    # Find if there is an mp4 file
    for file in metadata.get("files", []):
        if file["name"].endswith((".mp4")):
            mp4 = True
            break
    
    # Download a sutiable format, priortizing mp4
    for file in metadata.get("files", []):
        if (file["name"].endswith((".mkv", ".avi")) and not mp4) or (file["name"].endswith((".mp4"))):
            file_url = f"https://archive.org/download/{identifier}/{file['name']}"
            local_file_path = os.path.join(dest_folder, file["name"])
            
            print(f"Downloading: {file_url}")
            with requests.get(file_url, stream=True) as r:
                # Get total size of the file
                total_size = int(r.headers.get('content-length', 0))
                
                # Use tqdm for the progress bar
                with tqdm(total=total_size, unit='B', unit_scale=True, desc=file["name"]) as progress_bar:
                    with open(local_file_path, "wb") as f:
                        for chunk in r.iter_content(chunk_size=8192):
                            f.write(chunk)
                            progress_bar.update(len(chunk))
            
            print(f"Downloaded to: {local_file_path}")
            return local_file_path
    
    raise ValueError("No suitable movie files found.")

def get_imdb_id(movie_title, year=None):
    """Fetch the IMDb ID for a movie using the OMDb API."""
    base_url = "http://www.omdbapi.com/?i=tt3896198&apikey={}".format(OMDB_API_KEY)
    params = {
        "t": movie_title,
        "y": year,  # Optional year filter
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if response.status_code == 200 and data.get("Response") == "True":
        return data.get("imdbID")  # Return IMDb ID like 'tt12801262'
    else:
        print(f"Error fetching IMDb ID: {data.get('Error', 'Unknown error')}")
        return None

def rename_and_move(file_path, movie_title, year=None):
    """Rename and move the file to match Jellyfin's naming conventions with IMDb ID tag."""
    # Fetch IMDb ID
    imdb_id = get_imdb_id(movie_title, year)
    imdb_tag = f" [imdbid-{imdb_id}]" if imdb_id else ""
    
    # Format folder and file names
    formatted_title = movie_title.replace(" ", " ")
    folder_name = f"{formatted_title} ({year})" if year else formatted_title
    dest_folder = os.path.join(JELLYFIN_LIBRARY_PATH, folder_name)
    os.makedirs(dest_folder, exist_ok=True)
    
    # Format new filename
    new_filename = f"{formatted_title} ({year}){imdb_tag}{os.path.splitext(file_path)[-1]}"
    new_file_path = os.path.join(dest_folder, new_filename)
    
    # Move and rename file
    shutil.move(file_path, new_file_path)
    print(f"File moved and renamed to: {new_file_path}")
    return new_file_path

if __name__ == '__main__':
    # === MAIN SCRIPT ===
    try:
        print(f"Searching for: {MOVIE_TITLE}")
        results = search_movie(MOVIE_TITLE, year=MOVIE_YEAR)
        if not results:
            print("Movie not found.")
            exit(1)

        for index, movie in enumerate(results):
            print(f"Index: {index}, Title: {movie['title']}, Year: {movie.get('year', 'Unknown')}, Creator: {movie.get('creator', 'Unknown')}, URL: https://archive.org/details/{movie['identifier']}")

        ind = int(input('Choose an index: '))
        result = results[ind]

        identifier = result["identifier"]
        title = result["title"]
        print(f"Found: {title} (Identifier: {identifier})")
        title_mod = input('Would you like to change the title? ')
        
        if title_mod != 'n' and title_mod != '':
            title = title_mod
            print('Title changed to {}'.format(title))
        
        temp_download_folder = "/tmp"  # Temporary folder for downloads
        downloaded_file = download_movie(identifier, temp_download_folder)
        
        renamed_file = rename_and_move(downloaded_file, title, movie.get('year', None))
        print("Process complete. File ready for Jellyfin.")
    except Exception as e:
        print(f"ERROR: {e}")