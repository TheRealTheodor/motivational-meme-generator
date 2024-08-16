"""Module containing a class for file handler."""

import os
import random
import uuid


class FileHandler:
    """Class to handle files operations for this project."""

    QUOTE_FILES = [
        "./_data/DogQuotes/DogQuotesTXT.txt",
        "./_data/DogQuotes/DogQuotesDOCX.docx",
        "./_data/DogQuotes/DogQuotesPDF.pdf",
        "./_data/DogQuotes/DogQuotesCSV.csv",
    ]

    TEMP_FOLDER = "./tmp"

    @classmethod
    def pick_image(cls, folder_path: str) -> str:
        """Pick random image for given folder path."""
        imgs = []
        for root, _, files in os.walk(folder_path):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
        return img

    @classmethod
    def check_existing_folder(cls, folder: str) -> bool:
        """Check if the output folder of instance of MemeEngine exists."""
        listed_files = os.listdir()
        if folder.removeprefix("./") in listed_files:
            return True
        return False

    @classmethod
    def create_folder(cls, folder: str) -> None:
        """Create output folder."""
        os.mkdir(folder)

    @classmethod
    def create_rnd_in_temp(cls, file_extension: str) -> str:
        """Create random file name with given extension in temp folder."""
        return cls.TEMP_FOLDER + str(uuid.uuid4()) + file_extension
