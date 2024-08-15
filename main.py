"""Script for generating meme."""

import argparse
import os
import random

from MemeGenerator.file_handler import FileHandler
from MemeGenerator.meme_generator import MemeEngine
from QuoteEngine.ingestors import Ingestor
from QuoteEngine.quote_model import QuoteModel


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    if path is None:
        img = FileHandler.pick_image(folder_path="./_data/photos/dog")
    else:
        img = path

    if body is None:
        quotes = FileHandler.list_of_all_available_quotes()
        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception("Author Required if Body is Used")
        quote = QuoteModel(body, author)

    meme = MemeEngine("./meme_imgs")
    output_path = meme.make_meme(image_path=img, quote=quote)
    return output_path


if __name__ == "__main__":
    arparser = argparse.ArgumentParser(
        description="A simple program to create meme out of image with a quote."
    )
    arparser.add_argument(
        "--path",
        required=False,
        help="A path to image from which the meme will be created. If no value is given, random image from ./_data/photos/dogs/ is picked.",
    )
    arparser.add_argument(
        "--body",
        required=False,
        help="A body of quote to caption image. If no value is given, random quote from ./_data/DogQuotes/ is picked.",
    )
    arparser.add_argument(
        "--author",
        required=False,
        help="An author if quote. Required if --body is used.",
    )
    args = arparser.parse_args()
    print(generate_meme(path=args.path, body=args.body, author=args.author))
