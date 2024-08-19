# Motivational meme generator
This project creates Meme Generator:
1. Create a meme out of your file with given quote body and it author or generate random one through Command Line Interface (CLI).
2. Create a random meme in simple flask app or create meme out of picture from given URL.

# Requirements
To run this project you will need to create a virtual environment with python dependencies in ``requirements.txt``.

1. To run meme-generator from CLI you just need to type `python3 main.py` to generate random meme into a folder `meme_imgs/`. To use additional options thorugh CLI you can type `python3 main.py --help`. Some of the examples are `python3 main.py --body "I can eat that." --author "Good boi"` or `python3 main.py --path _data/photos/dog/xander_1.jpg`.
2. To use the simple web application you need to type in your terminal export `FLASK_APP=app.py` and then `flask run --host 0.0.0.0 --port 8080 --reload`. This will launch the application at [localhost](http://localhost:8080/create). You can either generate a random meme or you can create your own meme from JPG/PNG picture from given URL.
