from PIL import Image, ImageDraw, ImageFont
import random
import os


class MemeEngine:
    """Class that generates the picture with quote on it"""

    def __init__(self, output_dir):
        self.output_dir = output_dir
        self.img_name = 'meme_img.png'
        

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Generate meme and return output path to meme file"""
        
        if width > 500:
            raise Exception("image width must be <= 500 pixels")
        
        try:
         img = Image.open(img_path)
        except Exception:
            raise Exception("file path not valid")
        
        # resize image and preserve ratio
        ratio = width/float(img.size[0])
        height = int(ratio*float(img.size[1]))
        img = img.resize((width,height),Image.NEAREST)

        # write text on image
        draw = ImageDraw.Draw(img)
        font_size = 5
        font = ImageFont.truetype("Ubuntu-B.ttf", font_size)
        # portion of image width that the text should cover
        img_fraction_width = 0.50

        if font.getsize(author) < font.getsize(text):
            quote_txt = text
        else:
            quote_txt = author

        # https://stackoverflow.com/questions/4902198/pil-how-to-scale-text-size-in-relation-to-the-size-of-the-image
        # determine fontsize based on img_fraction to be covered
        while font.getsize(quote_txt)[0] < img_fraction_width*img.size[0]:
            # iterate until the text size is just larger than the criteria
            font_size += 1
            font = ImageFont.truetype("Ubuntu-B.ttf", font_size)


        # determine random position to place quote body within image
        x_body = random.randint(0,int(img.width*(1-(img_fraction_width+0.1))))
        y_body = random.randint(int((0+(font_size*2))), int(img.height - (font_size*4)))

        # determine position to place quote author
        x_author = x_body + (int(font.getsize(text)[0] / 4))
        y_author =  y_body + (font_size + 5)

        # define fillcolor and shadow color for outline
        # outline configuration adapted from:
        # https://stackoverflow.com/questions/41556771/is-there-a-way-to-outline-text-with-a-dark-line-in-pil
        fillcolor = "white"
        shadowcolor = "black"

        # draw body of quote on image
        # outline body
        draw.text((x_body-1, y_body), f'"{text}"', font=font, fill=shadowcolor)
        draw.text((x_body+1, y_body), f'"{text}"', font=font, fill=shadowcolor)
        draw.text((x_body, y_body-1), f'"{text}"', font=font, fill=shadowcolor)
        draw.text((x_body, y_body+1), f'"{text}"', font=font, fill=shadowcolor)
        # text body 
        draw.text((x_body,y_body), f'"{text}"', font=font, fill=fillcolor)

        # draw author of quote on image
        # outline author 
        draw.text((x_author-1, y_author), f' - {author}', font=font, fill=shadowcolor)
        draw.text((x_author+1, y_author), f' - {author}', font=font, fill=shadowcolor)
        draw.text((x_author, y_author-1), f' - {author}', font=font, fill=shadowcolor)
        draw.text((x_author, y_author+1), f' - {author}', font=font, fill=shadowcolor)

        # text author 
        draw.text((x_author, y_author), f' - {author}', font=font, fill=fillcolor)

        output_path = f'{self.output_dir}/{self.img_name}'
        img.save(os.path.join(self.output_dir, self.img_name))

        return output_path

    