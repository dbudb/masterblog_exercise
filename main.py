import json

from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)


def load_posts():
    """Load blog posts from the JSON file."""
    with open("blog_posts.json", "r", encoding="utf-8") as file:
        return json.load(file)


def save_posts(posts):
    """Save blog posts to the JSON file."""
    with open("blog_posts.json", "w", encoding="utf-8") as file:
        json.dump(posts, file, indent=4)


@app.route("/")
def index():
    """Display all blog posts."""
    posts = load_posts()
    return render_template("index.html", posts=posts)


@app.route("/add", methods=["GET", "POST"])
def add():
    """Display the add form or create a new blog post."""
    if request.method == "POST":
        posts = load_posts()

        author = request.form.get("author")
        title = request.form.get("title")
        content = request.form.get("content")

        new_id = max((post["id"] for post in posts), default=0) + 1

        posts.append(
            {
                "id": new_id,
                "author": author,
                "title": title,
                "content": content,
            }
        )

        save_posts(posts)
        return redirect(url_for("index"))

    return render_template("add.html")


@app.route("/delete/<int:post_id>")
def delete(post_id):
    """Delete a blog post and return to the homepage."""
    posts = load_posts()

    posts = [
        post for post in posts
        if post["id"] != post_id
    ]

    save_posts(posts)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)