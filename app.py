import os
import random

import requests
from flask import Flask, abort, render_template, request
from MemeGenerator.meme_generator import MemeEngine

from MemeGenerator.file_picker import FileHandler

app = Flask(__name__)

meme = MemeEngine("./static")


def setup():
    """Load all resources"""

    quotes = FileHandler.list_of_all_available_quotes()
    imgs = FileHandler.list_all_images()
    return quotes, imgs


quotes, imgs = setup()


@app.route("/")
def meme_rand():
    """Generate a random meme"""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(image_path=img, quote=quote)
    return render_template("meme.html", path=path)


@app.route("/create", methods=["GET"])
def meme_form():
    """User input for meme information"""
    return render_template("meme_form.html")


@app.route("/create", methods=["POST"])
def meme_post():
    """Create a user defined meme"""

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    path = None

    return render_template("meme.html", path=path)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
