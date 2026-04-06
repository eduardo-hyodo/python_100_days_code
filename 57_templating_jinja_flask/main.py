from flask import Flask, render_template
import datetime 

app = Flask(__name__)


@app.route("/")
def hello_world():
    current_year = datetime.date.today().year
    return render_template("index.html", year=current_year)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


