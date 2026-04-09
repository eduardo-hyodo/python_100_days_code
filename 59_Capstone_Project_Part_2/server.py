from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def index():
    blog_posts = get_blog_posts()
    return render_template("index.html", posts=blog_posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:post_id>")
def show_post(post_id):
    blog_posts = get_blog_posts()
    post = next((p for p in blog_posts if p["id"] == post_id), None)
    print(post)
    return render_template("post.html", post=post)


def get_blog_posts():    
    response_blog = requests.get("https://api.npoint.io/e5d27e59c841502a02c0")
    response_blog.raise_for_status()
    blog_posts =  response_blog.json()
    return blog_posts

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


