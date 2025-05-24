import json, pprint

with open("movie_data.json") as file:
    movie_data = json.load(file)

sorted_movies = sorted(movie_data, key=lambda movie_id: movie_data[movie_id]["vote_average"], reverse=True)

for movie_id in sorted_movies:
    print(movie_data[movie_id]["title"], movie_data[movie_id]["vote_average"])