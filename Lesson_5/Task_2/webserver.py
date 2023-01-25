from flask import Flask, render_template, request, redirect
from datetime import datetime


app = Flask("News")


@app.route("/")
def index():
    dataFile = open("news.txt", "r")
    text = dataFile.read()
    dataFile.close
    return render_template("index.html", text=text)


@app.route("/editor")
def editor():
    return render_template("editor.html")


@app.route("/process")
def input_file():
    dataFile = open("news.txt", "a")
    dataFile.write('<div class="center"><h1>' + request.args.get("title") + '</h1><h4>' + getTime() + '</h4><h2>'+ request.args.get("text") +'</h2></div>')
    return redirect("/")


def getTime():
    time = datetime.now()
    time = time.strftime(f'{str(time.year)}-{str(time.month)}-{str(time.day)} ' + "%H:%M:%S")
    return time


app.run(host="0.0.0.0", port=8081)