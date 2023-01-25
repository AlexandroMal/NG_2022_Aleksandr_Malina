from flask import Flask, request, render_template, redirect
from component import * 
from dataBase import *


app = Flask("Info")


@app.route('/')
def main():
    return render_template("index.html")


@app.route('/procces')
def procces():
    list = request.args.getlist("components")
    checkElements(list)
    return render_template("index.html", usertable=returnDataBase())


app.run(host="0.0.0.0", port='8080')