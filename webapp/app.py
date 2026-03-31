from flask import Flask, render_template, request
import requests

app = Flask(__name__)

currency_course = {
    'EUR': 77,
    'USD': 63,
    'UZS': 0.00692,
    'GBP': 98,

}

@app.route("/")
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

@app.route("/reg", methods=["GET", "POST"])
def reg():
    try:
        form_data = dict(request.args)
        data1 = form_data['username']
        data2 = form_data['password']
    except:
        print("Данных нет!")
    else:
        print(data1)
        print(data2)
    return render_template("reg.html")

@app.route("/converter")
def converter():
    data = dict(request.args)
    if len(data) > 0:
        amount = int(data["amount"])
        currency = data["currency"]
        return render_template("converter.html", data={
            "new_amount": amount * currency_course[currency]
        })
    return render_template("converter.html", data={"new_amount":0})

app.run()
