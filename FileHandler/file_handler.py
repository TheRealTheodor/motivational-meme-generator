"""Module containing a class for file handler."""

import os
import random
import uuid
from typing import List


class FileHandler:
    """Class to handle files operations for this project."""

    QUOTE_FILES = [
        "./_data/DogQuotes/DogQuotesTXT.txt",
        "./_data/DogQuotes/DogQuotesDOCX.docx",
        "./_data/DogQuotes/DogQuotesPDF.pdf",
        "./_data/DogQuotes/DogQuotesCSV.csv",
    ]

    TEMP_FOLDER = "./tmp"

    @staticmethod
    def pick_image(folder_path: str) -> str:
        """Pick random image for given folder path."""
        imgs = []
        for root, _, files in os.walk(folder_path):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
        return img

    @staticmethod
    def check_existing_folder(folder: str) -> bool:
        """Check if the output folder of instance of MemeEngine exists."""
        listed_files = os.listdir()
        if folder.removeprefix("./") in listed_files:
            return True
        return False

    @staticmethod
    def create_folder(folder: str) -> None:
        """Create output folder."""
        os.mkdir(folder)

    @classmethod
    def create_rnd_in_temp(cls, file_extension: str) -> str:
        """Create random file name with given extension in temp folder."""
        return cls.TEMP_FOLDER + str(uuid.uuid4()) + file_extension

    @staticmethod
    def list_all_images(folder_path: str = "./_data/photos/dog/") -> List[str]:
        """List all images available for given path."""
        img_list = os.listdir(path=folder_path)
        return [folder_path + img for img in img_list]
