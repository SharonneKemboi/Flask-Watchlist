from email import message
from turtle import title
from flask import render_template
from app import app

#Views
@app.route('/')
def index():
          
    title = 'Home - Welcome To Atarah Movie Review '  
    return render_template('index.html', title = title)   
    

@app.route('/movie/<int:movie_id>')
def movie(movie_id):

    return render_template('movie.html',id = movie_id)