from flask import Flask, render_template
import requests
from post import Post
from pprint import pprint


# getting the blogs

blog_endpoint = "https://api.npoint.io/c790b4d5cab58020d391"
posts = requests.get(url=blog_endpoint)

# creating the flask app
app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template('index.html', all_posts=posts)

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)