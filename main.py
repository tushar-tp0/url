from flask import Flask, render_template, request, redirect
import random
import string
import json
import os

app = Flask(__name__)

FILE = "data.json"

if os.path.exists(FILE):
    f = open(FILE, "r")
    urls = json.load(f)
    f.close()
else:
    urls = {}


def save():
    f = open(FILE, "w")
    json.dump(urls, f)
    f.close()


def genCode():
    chars = string.ascii_letters + string.digits
    code = ""
    for i in range(6):
        code = code + random.choice(chars)
    return code


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        url = request.form.get("url")
        alias = request.form.get("alias", "")

        if not url:
            return render_template("index.html", urls=urls, error="Please enter a url!")

        if not url.startswith(("http://", "https://")):
            url = "http://" + url

        if alias != "":
            code = alias
        else:
            code = genCode()
            while code in urls:
                code = genCode()

        if code in urls:
            return render_template("index.html", urls=urls, error="That alias is already taken, try a different one!")
        urls[code] = {"original": url, "clicks": 0}
        save()
        print("added new url ->", code)

        return redirect("/")

    return render_template("index.html", urls=urls, error=None)


@app.route("/<code>")
def goToUrl(code):
    if code in urls:
        urls[code]["clicks"] = urls[code]["clicks"] + 1
        save()
        return redirect(urls[code]["original"])
    else:
        return "<h2>Oops! That short code doesn't exist :(</h2><a href='/'>Go back</a>"


if __name__ == "__main__":
    app.run(debug=True, port=5000)