from flask import Flask, request, redirect, render_template
from database import *

app = Flask("Chat")


@app.route('/')
def outAll():
    return render_template("index.html", users=returnDataBase())

@app.route('/updates')
def add():
    login = request.args.get("login_input")
    message = request.args.get("message_input")
    addToDataBase(login,message)
    return redirect('/')

@app.route("/updatepage")
def update():   
    user = returnDataBase()
    return user
    
app.run(host="0.0.0.0", port="8080")
    



