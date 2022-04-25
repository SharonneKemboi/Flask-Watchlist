from email import message
from flask import render_template
from app import app

#Views
@app.route('/')
def index():
          
    message = 'Hello this my first Flask Project'      
    return render_template('index.html',message = message)
