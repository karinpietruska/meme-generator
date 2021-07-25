import random
import os
import requests
from flask import Flask, render_template, abort, request

from MemeGenerator import MemeEngine
from QuoteEngine import Ingestor

app = Flask(__name__)


meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for in_file in quote_files:
        quotes.extend(Ingestor.parse(in_file))

    images_path = "./_data/photos/dog/"

    imgs = []     
    for root, dirs, files in os.walk(images_path):
        for name in files:
            if name.endswith('.jpg'):
                imgs.append(os.path.join(root, name))
    return quotes, imgs


quotes, imgs = setup()

@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img_path = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img_path,quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    img_url = request.form["image_url"]
    body = request.form["body"]
    author = request.form["author"]

    try:       
        tmp_img_path = "./temp_img.jpg"
        img_con = requests.get(img_url,stream=True).content
        with open(tmp_img_path,'wb') as f:
            f.write(img_con)
    except Exception:
        print("link to image not working")
        return render_template('meme_form.html')
    
    path = meme.make_meme(tmp_img_path, body, author)
    os.remove(tmp_img_path)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
