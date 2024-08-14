import random
import uuid

from PIL import Image, ImageDraw, ImageFont

from QuoteEngine.quote_model import QuoteModel


class MemeEngine:

    def __init__(self, output_folder) -> None:
        self._output_folder = output_folder

    def make_meme(self, image_path: str, quote: QuoteModel, width=500) -> str:
        image = Image.open(image_path)
        new_height = (width / image.size[0]) * image.size[-1]
        resized_image = image.resize(size=(width, new_height))
        my_font = ImageFont.truetype(
            "/usr/share/fonts/truetype/ubuntu/UbuntuMono-R.ttf", 15
        )
        path_to_output_image = self._output_folder + str(uuid.uuid4()) + ".jpeg"
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
        resized_image.save(path_to_output_image)
        return path_to_output_image
