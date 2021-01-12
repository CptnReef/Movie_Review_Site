from flask import Flask, request, render_template
from pprint import PrettyPrinter
from bs4 import BeautifulSoup

import mongoengine as db
import imdb
import json
import os
import requests
import random

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('home.html')


# database_name = "quickstart"
# DB_URI = "mongodb+srv://MongoDBUser:wB2ULBQwOaFYLkKU@pythoncluster.zgpvn.mongodb.net/MongoDBUser?retryWrites=true&w=majority"
# db.connect(DB_URI)

# print(movies[0].keys())

# ------------ Search for a movie title
moviesDB = imdb.IMDb()

movies = moviesDB.search_movie('inception')

# print('seatching for "Inception":')
# for movie in movies:
#     title = movie ['title']
#     year = movie['year']
#     print(f'{title} - {year}')

# --------------------------------------



# ------------ List movie info
id = movies[0].getID()
movie = moviesDB.get_movie(id)

title = movie['title']
year = movie['year']
rating = movie['rating']
directors = movie['directors']
casting = movie['cast']

# print('Movie Info:')
# print(f'{title} - {year}')
# print(f'rating: {rating}')

# direcStr = ' '.join(map(str,directors))
# print(f'directors: {direcStr}')

# actors = ', '.join(map(str,casting))
# print(f'actors: {actors}')

# --------------------------------------



# ------------ List actor Info
id = casting[0].getID()
person = moviesDB.get_person(id)
bio = moviesDB.get_person_biography(id)

name = person['name']
birthDate = person['birth date']
height = person['height']
trivia = person['trivia']
titleRefs = bio['titlesRefs']

# print(f'name: {name}')
# print(f'birth date: {birthDate}')
# print(f'height: {height}')
# print(f'trivia: {trivia[0]}')

# titleRefsStr = ', '.join(map(str, titleRefs))
# print(f'bio title refs: {titleRefsStr}')

# --------------------------------------



# ------------ Top/Bottom 10 movies
top = moviesDB.get_top250_movies()
bottom = moviesDB.get_bottom100_movies()

# print('Top 10 movies:')
# for movie in top[0:9]:
#     print(movie)

# print('Bottom 10 movies:')
# for movie in bottom[0:9]:
#     print(movie)

# --------------------------------------




if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)