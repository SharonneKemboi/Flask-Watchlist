from turtle import title
from flask import render_template
from app import app
from .request import get_movies



#Views
@app.route('/')
def index():



    #get poplar movie
    popular_movies = get_movies('popular')
    upcoming_movies = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    
    title = 'Home - Welcome To Atarah Movie Review '  
    return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movies, now_showing = now_showing_movie)   
    

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    

    title = f'You are viewing {movie_id}'
    return render_template('movie.html',title = title)