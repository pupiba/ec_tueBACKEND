from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.get("/")
def main():
    return render_template("main.html", data={
        "name": "Антон"
    })

@app.get("/landscape")
def landscape():
    return render_template("landscape.html")

@app.get("/cats")
def cats():
    return render_template("cats.html")

@app.get("/dino")
def dino():
    return render_template("dino.html")

@app.get("/dog")
def dog():
    data = requests.get("https://dog.ceo/api/breeds/image/random")
    json_data = data.json()
    image = json_data.get("message")
    
    return render_template("dog.html",
                           data={"image": image})

app.run()
