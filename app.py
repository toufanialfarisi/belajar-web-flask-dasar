# import library flask
from flask import Flask, render_template

app = Flask(__name__)
app.jinja_env.filters["zip"] = zip


@app.route("/")
def index():
    # data dalam bentuk dictionary / json
    dataJson = {
        "no": [1, 2, 3, 4, 5],
        "buah": ["mangga", "apel", "semangka", "alpukat", "jeruk"],
        "hewan": ["ayam", "kucing", "gajah", "elang", "rusa"],
    }
    return render_template("index.html", data=dataJson)


if __name__ == "__main__":
    app.run(debug=True)