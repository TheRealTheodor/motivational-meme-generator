import os
import random
import uuid

import requests
from flask import Flask, abort, render_template, request

from MemeGenerator.file_handler import FileHandler
from MemeGenerator.meme_generator import MemeEngine
from QuoteEngine.quote_model import QuoteModel

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

    # https://images.ctfassets.net/2y9b3o528xhq/4swf2qhcelEUWzKHaKne6C/d890de3220ea332fb42e9b8e5f7848fd/real-world-projects.png
    # https://images.ctfassets.net/2y9b3o528xhq/5sXS0Rr3MEr66P5elfYX7P/3728cc2d85c0979cb29d5cb291369038/mentor.jpg
    image_url = request.form.get("image_url")
    image_extension = "." + image_url.split(".")[-1]
    temp_folder = "./tmp/"
    quote = QuoteModel(body=request.form.get("body"), author=request.form.get("author"))

    response = requests.get(image_url)
    if response.status_code == 200:
        os.mkdir(temp_folder)
        full_path = temp_folder + str(uuid.uuid4()) + image_extension
        with open(full_path, "wb") as outfile:
            outfile.write(response.content)
        path = meme.make_meme(image_path=full_path, quote=quote)
        os.remove(full_path)
        os.rmdir(temp_folder)
    return render_template("meme.html", path=path)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
