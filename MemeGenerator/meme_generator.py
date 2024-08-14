import PIL
from QuoteEngine.quote_model import QuoteModel


class MemeGenerator:
    def __init__(self, output_folder) -> None:
        self._output_folder = output_folder

    @staticmethod
    def make_meme(image: str, quote_model: QuoteModel) -> str:
        pass
