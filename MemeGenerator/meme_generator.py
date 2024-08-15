"""Module with MemeEngine class used for generating captioned memes."""

import os
import random
import subprocess
import uuid

from PIL import Image, ImageDraw, ImageFont

from QuoteEngine.quote_model import QuoteModel


class MemeEngine:
    """Class to create captioned photos with quotes."""

    def __init__(self, output_folder) -> None:
        """Initialize new instance of MemeEngine.

        :param output_folder: Path string to folder where the meme will be saved.
        """
        self._output_folder = output_folder

    def check_existing_folder(self) -> bool:
        listed_files = os.listdir()
        if self._output_folder.removeprefix("./") in listed_files:
            return True
        return False

    def create_folder(self) -> None:
        subprocess.run(["mkdir", self._output_folder.removeprefix("./")])

    def make_meme(self, image_path: str, quote: QuoteModel, width=500) -> str:
        """Create a meme with body of quote and its author.

        :param image_path: Path string to image from which the meme will be made.
        :param quote: QuoteModel class containing the body of quote and author.
        :param width: Maximum width of captioned meme.
        """
        image = Image.open(image_path)
        new_height = (width / image.size[0]) * image.size[-1]
        resized_image = image.resize(size=(int(width), int(new_height)))
        my_font = ImageFont.truetype(
            "/usr/share/fonts/truetype/ubuntu/UbuntuMono-R.ttf", 15
        )
        path_to_output_image = self._output_folder + "/" + str(uuid.uuid4()) + ".jpeg"
        draw_resized_image = ImageDraw.Draw(resized_image)
        draw_resized_image.text(
            (
                random.randrange(width - 250),
                random.randrange(resized_image.size[-1]),
            ),
            quote.whole_quote,
            font=my_font,
            fill=(255, 255, 255),
        )
        if self.check_existing_folder():
            resized_image.save(path_to_output_image)
        else:
            self.create_folder()
            resized_image.save(path_to_output_image)
        return path_to_output_image
