"""This module contains abstract IngestorInterface and children ingestors for different file types."""

import csv
import os
import subprocess
from abc import ABC, abstractmethod
from typing import List

from docx import Document

from FileHandler.file_handler import FileHandler
from QuoteEngine.quote_model import QuoteModel


class IngestorInterFace(ABC):
    """Abstract parent class for different file importers."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check whether the ingestor class can ingest given file type.

        :param path: A path string to file.
        """
        extension = path.split(".")[-1]
        return extension in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str = "DogQuotes/DogQuotesCSV.csv") -> List[QuoteModel]:
        """Abstract method to be implemented in children classes.

        :param path: A path string to file.
        """
        pass


class CSVImporter(IngestorInterFace):
    """Class to import quotes from .csv files."""

    allowed_extensions = ["csv"]

    @classmethod
    def parse(cls, path: str = "_data/DogQuotes/DogQuotesCSV.csv") -> List[QuoteModel]:
        """Parse the information contained in row into QuoteModel.

        :param path: A path string to file.
        """
        if not cls.can_ingest(path=path):
            raise Exception("Cannot ingest.")

        with open(path, "r") as infile:
            whole_list = list(csv.reader(infile))
            whole_list.pop(0)
            list_of_quotes = []
            for quote in whole_list:
                list_of_quotes.append(QuoteModel(body=quote[0], author=quote[-1]))
            return list_of_quotes


class DOCXImporter(IngestorInterFace):
    """Class to import quotes from .docs files."""

    allowed_extensions = ["docx"]

    @classmethod
    def parse(
        cls, path: str = "_data/DogQuotes/DogQuotesDOCX.docx"
    ) -> List[QuoteModel]:
        """Parse the information contained in docx document into QuoteModel.

        :param path: A path string to file.
        """
        if not cls.can_ingest(path=path):
            raise Exception("Cannot ingest.")

        document = Document(path)
        return [
            QuoteModel.model_from_whole_quote(par.text)
            for par in document.paragraphs
            if par.text != ""
        ]


class TXTImporter(IngestorInterFace):
    """Class to import quotes from .txt files."""

    allowed_extensions = ["txt"]

    @classmethod
    def parse(cls, path: str = "_data/DogQuotes/DogQuotesTXT.txt") -> List[QuoteModel]:
        """Parse the information contained in row into QuoteModel.

        :param path: A path string to file.
        """
        with open(path, "r") as infile:
            return [QuoteModel.model_from_whole_quote(row) for row in infile]


class PDFImporter(IngestorInterFace):
    """Class to import quotes from .pdf files."""

    allowed_extensions = ["pdf"]

    @classmethod
    def parse(cls, path: str = "_data/DogQuotes/DogQuotesPDF.pdf") -> List[QuoteModel]:
        """Convert the .pdf file into a .txt file and use TXTImporter to import.

        :param path: A path string to file.
        """
        if not FileHandler.check_existing_folder(folder=FileHandler.TEMP_FOLDER):
            os.mkdir(FileHandler.TEMP_FOLDER)
        output_path = FileHandler.create_rnd_in_temp(file_extension=".txt")
        subprocess.run(["pdftotext", "-raw", "-nopgbrk", path, output_path])
        list_from_txt_importer = TXTImporter.parse(path=output_path)
        os.remove(output_path)
        os.rmdir(FileHandler.TEMP_FOLDER)
        return list_from_txt_importer


class Ingestor(IngestorInterFace):
    """General class to use importers for given file type."""

    IMPORTERS = [CSVImporter, DOCXImporter, PDFImporter, TXTImporter]

    @classmethod
    def parse(cls, path: str = "_data/DogQuotes/DogQuotesCSV.csv") -> List[QuoteModel]:
        """Use relevant importer for given file type.

        :param path: A path string to file.
        """
        for importer in cls.IMPORTERS:
            if importer.can_ingest(path=path):
                return importer.parse(path=path)

    @classmethod
    def list_of_all_available_quotes(cls) -> List[QuoteModel]:
        """Create list of all available quotes saved in different files."""
        quotes = []
        for quote_file in FileHandler.QUOTE_FILES:
            quotes.extend(cls.parse(quote_file))
        return quotes
