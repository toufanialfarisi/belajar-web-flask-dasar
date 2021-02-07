# import library flask
from flask import Flask, render_template
import data

app = Flask(__name__)
app.jinja_env.filters["zip"] = zip


@app.route("/")
def index():
    dataJson = data.data
    return render_template("index.html", data=dataJson)


if __name__ == "__main__":
    app.run(debug=True)