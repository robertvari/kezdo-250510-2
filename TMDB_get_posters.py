import tmdbsimple as tmdb
import os, requests
tmdb.API_KEY = '83cbec0139273280b9a3f8ebc9e35ca9'

POSTER_ROOT = "https://image.tmdb.org/t/p/w600_and_h900_bestv2"
POSTER_CACHE_FOLDER = r"C:\Work\PythonSuli\tmdb_images"

def main():
    movie_list = get_popular_movies()
    download_posters(movie_list)

def get_popular_movies():
    pass

def download_posters(movie_list):
    pass