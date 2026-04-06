from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello world</h1>"

@app.route("/home")
def home():
    return render_template("card.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
