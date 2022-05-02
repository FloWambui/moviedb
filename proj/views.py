from moviedb.app import app
from flask import Flask, render_template
from proj import movie
from proj import request



@app.route('/')
def home():
    movies=[]
    for i in range(11):
        req=request.Request() #creating an instance of the request cla


        data=req.request("https://api.themoviedb.org/3/movie/{}?api_key=f5b430665c1349c769f05717399a633a", 500+i)
        movies.append(movie.Movie(data["id"],data["title"],data["overview"],data["poster_path"],data["vote_average"],data["release_date"]))
        



    return render_template('index.html',datum=movies)