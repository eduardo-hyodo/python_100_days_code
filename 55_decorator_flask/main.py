from flask import Flask

app = Flask(__name__)
app.number = 5


@app.route("/")
def hello_world():
    print(app.number)
    return "<h1>Guess a number between 0 and 9</h1><br><image src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"

if __name__ == "__main__":
    app.run()
