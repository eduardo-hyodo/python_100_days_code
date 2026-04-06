from flask import Flask, render_template
import datetime 
import requests

app = Flask(__name__)


@app.route("/")
def hello_world():
    current_year = datetime.date.today().year
    return render_template("index.html", year=current_year)

@app.route("/guess/<guest_name>")
def guess(guest_name):
    parameters = {
        "name": guest_name,
    }
    response_gender = requests.get("https://api.genderize.io", params=parameters)
    response_gender.raise_for_status()
    data = response_gender.json()
    gender = data["gender"]
    response_age =  requests.get("https://api.agify.io", params=parameters)
    response_age.raise_for_status
    guest_age = response_age.json()["age"]

    return render_template("guess.html", guest_name=guest_name, guest_gender=gender, guest_age=guest_age)

@app.route("/blog")
def blog():
    blog_posts = get_blog_posts()
    return render_template("blog.html", posts=blog_posts)

@app.route("/post/<int:post_id>")
def post(post_id):
    blog_posts = get_blog_posts()
    post = next((p for p in blog_posts if p["id"] == post_id), None)
    print(post)
    return render_template("post.html", post=post)


def get_blog_posts():
    response_blog = requests.get("https://api.npoint.io/a0a7cb106868f0d7c692")
    response_blog.raise_for_status()
    blog_posts =  response_blog.json()
    return blog_posts

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


