import tmdbsimple as tmdb
import os, requests
tmdb.API_KEY = '83cbec0139273280b9a3f8ebc9e35ca9'

POSTER_ROOT = "https://image.tmdb.org/t/p/w600_and_h900_bestv2"
POSTER_CACHE_FOLDER = r"C:\Work\PythonSuli\tmdb_images"

def main():
    movie_list = get_popular_movies()
    download_posters(movie_list)

def get_popular_movies():
    movies = tmdb.Movies()
    popular_movies = movies.popular(page=1)
    return popular_movies["results"]

def download_posters(movie_list):
    for movie_data in movie_list:
        if not movie_data.get("poster_path"): continue

        poster_url = f"{POSTER_ROOT}{movie_data.get('poster_path')}"
        image_file_path = os.path.join(POSTER_CACHE_FOLDER, movie_data.get('poster_path')[1:])
        
        print(f"Downloading: {poster_url}")

        image_data = requests.get(poster_url).content
        with open(image_file_path, "wb") as file:
            file.write(image_data)


main()