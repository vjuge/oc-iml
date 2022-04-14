from flask import Flask
from markupsafe import escape
from flask import render_template
from flask import request, redirect
from utils.lib import predict


app = Flask(__name__)

# ret = predict("configuring java for accessing database with jdbc is not working with JPA after upgrade of spring 5.1. despite having modified application.properties")
# print(ret)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route("/tags", methods=["GET", "POST"])
def tags():
    if request.method == "POST":

        req = request.form

        # username = req.get("username")
        # email = req["email"]
        # password = request.form["password"]
        inputtext = request.form["inputtext"]

        # You could also use 
        # password = request.form.get("password")

        # print(username)
        # print(email)
        # print(password)
        # print(inputtext)

        tags = predict(inputtext)
        print(tags)
        
        # return redirect(request.url)

        return render_template("tags.html", tags=tags, inputtext=inputtext)

    return render_template("tags.html")

