"""File for flask for running flask applicaation."""

import os
import random
from typing import List, Tuple

import requests
from flask import Flask, abort, render_template, request

from FileHandler.file_handler import FileHandler
from MemeGenerator.meme_generator import MemeEngine
from QuoteEngine.ingestors import Ingestor
from QuoteEngine.quote_model import QuoteModel

app = Flask(__name__)

meme = MemeEngine("./static")


def list_all_images(folder_path: str = "./_data/photos/dog/") -> List[str]:
    """List all images available for given path."""
    img_list = os.listdir(path=folder_path)
    return [folder_path + img for img in img_list]


def list_of_all_available_quotes() -> List[QuoteModel]:
    """Create list of all available quotes saved in different files."""
    quotes = []
    for quote_file in FileHandler.QUOTE_FILES:
        quotes.extend(Ingestor.parse(quote_file))
    return quotes


def setup() -> Tuple[List[QuoteModel], List[str]]:
    """Load all resources."""
    quotes = list_of_all_available_quotes()
    imgs = list_all_images()

    return quotes, imgs


quotes, imgs = setup()


@app.route("/")
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(image_path=img, quote=quote)
    return render_template("meme.html", path=path)


@app.route("/create", methods=["GET"])
def meme_form():
    """User input for meme information."""
    return render_template("meme_form.html")


@app.route("/create", methods=["POST"])
def meme_post():
    """Create a user defined meme."""
    image_url = request.form.get("image_url")
    image_extension = "." + image_url.split(".")[-1]
    quote = QuoteModel(body=request.form.get("body"), author=request.form.get("author"))

    response = requests.get(image_url)
    if response.status_code == 200:
        if not FileHandler.check_existing_folder(folder=FileHandler.TEMP_FOLDER):
            os.mkdir(FileHandler.TEMP_FOLDER)
        full_path = FileHandler.create_rnd_in_temp(file_extension=image_extension)
        with open(full_path, "wb") as outfile:
            outfile.write(response.content)
        path = meme.make_meme(image_path=full_path, quote=quote)
        os.remove(full_path)
        os.rmdir(FileHandler.TEMP_FOLDER)
    else:
        abort(code=response.status_code)
    return render_template("meme.html", path=path)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
