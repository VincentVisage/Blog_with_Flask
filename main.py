from flask import Flask, render_template
import requests
from postClass import Post

posts = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()
all_posts = []
for post in posts:
    post = Post(id=post["id"], title=post["title"], subtitle=post["subtitle"], body=post["body"])
    all_posts.append(post)


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route("/blog/<int:index>")
def get_post(index):
    req_post = None
    for post in all_posts:
        if post.id == index:
            req_post = post
    return render_template("post.html", post=req_post)



if __name__ == "__main__":
    app.run(debug=True, port=8002)
