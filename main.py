import json

from flask import Flask, render_template


app = Flask(__name__)


def load_posts():
    """Load and return all blog posts from the JSON file."""
    with open("blog_posts.json", "r", encoding="utf-8") as file:
        return json.load(file)


@app.route("/")
def index():
    """Display all blog posts."""
    blog_posts = load_posts()
    return render_template("index.html", posts=blog_posts)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)