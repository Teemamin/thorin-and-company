import os
import json
from flask import Flask, render_template, request  # request handles things like finding out wat method we used
# and returning our form object wen submitted.

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
    data = []
    with open ("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", pagetitle = "About" , company = data)


@app.route("/about/<member_name>")

 # So whenever we look at our about URL with something after it, that's going to be passed in to this view.  


def about_member(member_name):
    member = {}

    with open ("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data :
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member = member) # member = member, cos that is how we refer to it inside our template





@app.route("/contact", methods = ["GET", "POST"])
# by default flask view handles GET request but if we need to use other methods like POST or DELETE etc
# we will have to explicitly state that out route can accept that

def contact():
    if request.method == "POST":
        print(request.form)
    return render_template("contact.html", pagetitle = "Contact")

@app.route("/career")

def career():
    return render_template("career.html", pagetitle = "Career")


if __name__ == "__main__" :
 # __main__ is the name of the default module in Python. It's the first one that we run, soif this has not been imported 
 #  which it won't be it's going to be run directly -
 # then we want to run our app using these arguments that we're passing in here.
    app.run(host = os.environ.get("IP"), port = int(os.environ.get("PORT")), debug = True)
 