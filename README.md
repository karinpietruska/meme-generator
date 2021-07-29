# Meme Generator Project


A meme generator application that dynamically generates memes by overlaying a quote on an image. 

This project is part of the Udacity Intermediate Python Nanodegree Program.
Please contact Udacity regarding copyright or license. 

This project required the implementation of several modules:

The QuoteEngine module enables the ingestion of quotes from different file types including csv, pdf, docx and text files. 
An abstract base class named "IngestorInterface" is realized by several helper classes that implement the ingestion of each specific fily type: csv, pdf, docx and text files. 
Finally an Ingestor class is implemented that encapsulates these helper classes and given a specific file type as input, selects the correct helper class to ingest the quotes. 

The MemeEngine Module enables the actual generation of the meme. The submodule MemeGenerator loads an image file from disk, transforms it to the appropriate size and places a quote with body and author on a random location on the image. 

Finally the application is realized with a meme.py file that can be executed via the command line with three optional arguments: path to an image file, quote body and quote author. It returns a path to the location of the generated meme image. 

In addition, the application is also executable via a small Flask app (see how to run below). The Flask app uses the modules above to generate and display a random meme image. Alternatively the user can define an own meme image by entering an image url, a quote body and an author into the corresponding html template. 


## Installation 

First clone this repository and then install the dependencies. I used Python version 3.9.0 and I recommend installing the the dependencies into a new conda environment or virtualenv environment. 

```bash
git clone https://github.com/karinpietruska/meme-generator.git
pip install -r requirements.txt

```

## How to use: Flask App 

From within the src folder run the app.py

```bash
python3 app.py

```

Then open the link that appears in the terminal. 
You will see a randomly generated meme similar to the following picture. 

<p align="center">
<img src="./img/meme_example1.png" alt="Starting meme of meme-generator."
width="50%"></p>


You have the choice of randomly generating another meme by clicking the "Random" button below the image. Alternatively, you can create your own meme by clicking on the "Creator" button. 
This opens the following template and you are asked to enter the image url, the body of the quote and the author of the quote.

<p align="center">
<img src="./img/meme_example2.png" alt="Meme generator with option to create own meme."
width="50%"></p>

For instance, I used the free to use dog picture in the following link: 
https://libreshot.com/wp-content/uploads/2014/01/white-dog-eats.jpg

This image was taken by Martin Vorel and is free for download and commercial use with a CC0-Public Domain license. 
Link to source website: https://libreshot.com/white-dog-eats-bone-2/

I used the above image with a quote text as displayed in the image below. 

<p align="center">
<img src="./img/meme_example3.png" alt="Meme generator with option to create own meme."
width="50%"></p>

Then click the "Create Meme!" button and you see the created meme image: 

<p align="center">
<img src="./img/meme_example4.png" alt="Meme generated with the creator option."
width="50%"></p>

## How to use: Command Line 

The meme generator can also be executed via command line. 

First make sure you are within the src folder. For random generation of a meme enter:

```bash
python3 meme.py

```

To generate a meme with your own text or locally saved image, enter three additional arguments via the command line. 
-- path: the path to the image file
-- body: the quote body
-- author: the author of the quote

For instance, to generate a meme with your own text with one of the dog images proviced enter:

```bash
python3  meme.py --path _data/photos/dog/xander_1.jpg --body "bark or be barked at" --author "dog wisdom"

```

The app returns the path to the saved image. In the current implementation, it is saved at:
./tmp/meme_img.png

The image of the above command line input looks like this:

<p align="center">
<img src="./img/meme_example5.png" alt="Meme generated with command line entry."
width="50%"></p>