from flask import Flask, request, redirect, render_template, url_for
from pprint import PrettyPrinter
import mongoengine as db
import imdb 
import json
import os
import requests
import random

# database_name = "quickstart"
# DB_URI = "mongodb+srv://MongoDBUser:wB2ULBQwOaFYLkKU@pythoncluster.zgpvn.mongodb.net/MongoDBUser?retryWrites=true&w=majority"
# db.connect(DB_URI)

############################################################
# SETUP
############################################################

app = Flask(__name__)

moviesDB = imdb.IMDb()

movies = moviesDB.search_movie('inception')


print(movies)

posters =  []
for movie in movies:
    posters.append(movie['full-size cover url'])


id = movies[0].getID()
movie = moviesDB.get_movie(id)

title = movie['title']
year = movie['year']
rating = movie['rating']
directors = movie['directors']
casting = movie['cast']
poster = movie['cover url']
full_poster = movie['full-size cover url']

top = moviesDB.get_top250_movies()
bottom = moviesDB.get_bottom100_movies()

############################################################
# MOVIE TITLE SEARCH
############################################################

@app.route('/')
def homepage():
    # type_in = request.form.get('movie_title')
    
    id = casting[0].getID()

    person = moviesDB.get_person(id)
    bio = moviesDB.get_person_biography(id)

    name = person['name']
    trivia = person['trivia']

    context = {        
        'movies': movies,
        'title': title,
        'year': year,
        'rate': rating,
        'cast': casting,
        'poster': posters,
        'big_poster': full_poster,
        'top': top,
        'bottom': bottom,
        'name': name,
        'trivia': trivia,
    }

    return render_template('home.html',**context)

############################################################
# MOVIE PAGE
############################################################

@app.route('/movie_page', methods=['GET', 'POST'])
def moviepage():
    
    id = casting[0].getID()

    person = moviesDB.get_person(id)
    bio = moviesDB.get_person_biography(id)

    name = person['name']
    trivia = person['trivia']
    movie_data = movies
        
    context = {
        'movies': movie_data,
        'title': title,
        'cast': casting,
        'poster': poster,
        'rate': rating,
        'big_poster': full_poster,
        'top': top,
        'bottom': bottom,
        'name': name,
        'trivia': trivia
    }

    return render_template('movie_page.html',**context)


############################################################
# SEARCH
############################################################

# @app.route('/search', methods=['GET', 'POST'])
# def search():
    
#     if request.method == 'POST':
        
#         context = {
#             'search': request.form.get('title_name'),
#             'title': title,
#             'cover': poster,
#         }

#         return render_template('search.html',**context)


############################################################
# DEBUG
############################################################

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)









############################################################
# MOVIE DETAILS / REVIEW PAGE
############################################################

# print('Movie Info:')
# print(f'{title} - {year}')
# print(f'rating: {rating}')

# direcStr = ' '.join(map(str,directors))
# print(f'directors: {direcStr}')

# actors = ', '.join(map(str,casting))
# print(f'actors: {actors}')


############################################################
# ACTOR INFO
############################################################


# print(f'name: {name}')
# print(f'trivia: {trivia[0]}')

# titleRefsStr = ', '.join(map(str, titleRefs))
# print(f'bio title refs: {titleRefsStr}')


