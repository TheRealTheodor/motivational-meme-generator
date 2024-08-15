"""Module containing a class for random image picker."""

import os
import random
from typing import List

from QuoteEngine.ingestors import Ingestor
from QuoteEngine.quote_model import QuoteModel


class FileHandler:
    QUOTE_FILES = [
        "./_data/DogQuotes/DogQuotesTXT.txt",
        "./_data/DogQuotes/DogQuotesDOCX.docx",
        "./_data/DogQuotes/DogQuotesPDF.pdf",
        "./_data/DogQuotes/DogQuotesCSV.csv",
    ]

    @classmethod
    def pick_image(cls, folder_path: str) -> str:
        imgs = []
        for root, _, files in os.walk(folder_path):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
        return img

    @classmethod
    def list_all_images(cls, folder_path: str = "./_data/photos/dog/") -> List[str]:
        img_list = os.listdir(path=folder_path)
        return [folder_path + img for img in img_list]

    @classmethod
    def list_of_all_available_quotes(cls) -> List[QuoteModel]:
        quotes = []
        for quote_file in cls.QUOTE_FILES:
            quotes.extend(Ingestor.parse(quote_file))
        return quotes
