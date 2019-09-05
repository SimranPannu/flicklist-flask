import random
from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    # choose a movie by invoking our new function
    movie = get_random_movie()

    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + movie + "</li>"
    content += "</ul>"
   
    
    

    tomorrow_movie = get_random_movie()
    # TODO: pick another random movie, and display it under
    # the heading "<h1>Tommorrow's Movie</h1>"
    content += "<h1>Tommorrow's Movie</h1>"
    content += "<ul>"
    content += "<li>" + tomorrow_movie + "</li>"
    content += "</ul>"

    return content

def get_random_movie():
    # TODO: make a list with at least 5 movie titles
    my_list=["The Big Lebowski","Fast and Furios","The Lion king","Aladdin","Toy Story"]
    # TODO: randomly choose one of the movies, and return it
    movie=random.randint(0,4)
    return my_list[movie]


app.run()
