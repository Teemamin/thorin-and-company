import os
from flask import Flask, render_template

app = Flask(__name__) 
# we can use __name__ which is a built-in Python variable. Flask needsthis so that it knows where to look for templates and static files. 
@app.route("/")
# using the app.route decorator. In Python, a decorator starts with the @ sign, which is
# also called pie notation. And, effectively, a decorator
# is a way of wrapping functions.
# So, when we try to browse to the root directory as indicated by the "/", then
# flask triggers the index function underneath and returns the "Hello, World"

def index():
    return render_template("index.html")

@app.route("/about")

def about():
    return render_template("about.html")

@app.route("/contact")

def contact():
    return render_template("contact.html")


if __name__ == "__main__" :
 # __main__ is the name of the default module in Python. It's the first one that we run, soif this has not been imported 
 #  which it won't be it's going to be run directly -
 # then we want to run our app using these arguments that we're passing in here.
    app.run(host = os.environ.get("IP"), port = int(os.environ.get("PORT")), debug = True)
 