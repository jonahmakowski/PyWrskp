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
    """
    Searches for a movie on the Internet Archive based on the given title and optional year.

    Args:
        title (str): The title of the movie to search for.
        year (int, optional): The year of the movie to search for. Defaults to None.

    Returns:
        list: A list of dictionaries containing movie information (identifier, title, creator, year) if found.
        None: If no movies are found matching the search criteria.
    """
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
    """
    Downloads a movie from the Internet Archive given its identifier and saves it to the specified destination folder.
    The function prioritizes downloading an MP4 file if available. If no MP4 file is found, it will download an MKV or AVI file.
    Args:
        identifier (str): The unique identifier of the movie on the Internet Archive.
        dest_folder (str): The destination folder where the movie file will be saved.
    Returns:
        str: The local file path where the movie was downloaded.
    Raises:
        requests.exceptions.RequestException: If there is an issue with the HTTP request.
        ValueError: If no suitable movie files are found.
    """
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
    """
    Fetches the IMDb ID for a given movie title using the OMDB API.
    Args:
        movie_title (str): The title of the movie.
        year (int, optional): The release year of the movie to narrow down the search. Defaults to None.
    Returns:
        str: The IMDb ID of the movie if found, otherwise None.
    Raises:
        None: This function does not raise any exceptions, but it prints an error message if the request fails.
    """
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
    """
    Renames and moves a file to a new directory based on the movie title and year.
    Args:
        file_path (str): The path to the file that needs to be renamed and moved.
        movie_title (str): The title of the movie.
        year (int, optional): The release year of the movie. Defaults to None.
    Returns:
        str: The new file path after renaming and moving the file.
    Raises:
        Exception: If there is an error in fetching the IMDb ID or moving the file.
    """
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
