# Documentation for src/jellyfinDownload/main.py

**Movie Downloader Script Documentation**

**Summary**
------------

This script is designed to download movies from the Internet Archive and move them to a specified destination folder based on their title and year. It uses various APIs, including OMDB API and requests library, to fetch movie information and download files.

**Functions and Classes**
------------------------

### search_movie(title, year=None)

*   Description: Searches for a movie on the Internet Archive based on the given title and optional year.
*   Args:
    *   `title` (str): The title of the movie to search for.
    *   `year` (int, optional): The year of the movie to search for. Defaults to None.
*   Returns:
    *   list: A list of dictionaries containing movie information (identifier, title, creator, year) if found.
    *   None: If no movies are found matching the search criteria.

### download_movie(identifier, dest_folder)

*   Description: Downloads a movie from the Internet Archive based on its identifier and moves it to a specified destination folder.
*   Args:
    *   `identifier` (str): The identifier of the movie to download.
    *   `dest_folder` (str): The path to the destination folder.
*   Returns:
    *   str: The new file path after renaming and moving the file.

### get_imdb_id(movie_title, year=None)

*   Description: Fetches the IMDb ID for a given movie title and optional year.
*   Args:
    *   `movie_title` (str): The title of the movie.
    *   `year` (int, optional): The release year of the movie. Defaults to None.
*   Returns:
    *   str: The IMDb ID of the movie if found, otherwise None.

### rename_and_move(file_path, movie_title, year=None)

*   Description: Renames and moves a file based on its title and year.
*   Args:
    *   `file_path` (str): The path to the file that needs to be renamed and moved.
    *   `movie_title` (str): The title of the movie.
    *   `year` (int, optional): The release year of the movie. Defaults to None.
*   Returns:
    *   str: The new file path after renaming and moving the file.

**Main Script**
---------------

The main script is designed to:

1.  Search for a movie based on its title and download it from the Internet Archive.
2.  Move the downloaded file to a specified destination folder based on its title and year.
3.  Rename and move the file if necessary.

**Usage**
---------

To use this script, simply run it from the command line and follow the prompts:

```bash
python movie_downloader.py
```

This will start the download process. Follow the instructions to complete the download and rename/move process.

**Note**: This script assumes that you have Python installed on your system and that you have the necessary libraries (requests, OMDB API) available for import. Additionally, this script uses temporary folders to store downloaded files, so make sure you have write access to those directories.