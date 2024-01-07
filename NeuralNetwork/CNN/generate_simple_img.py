import random

import numpy as np
from PIL import Image, ImageDraw


def get_salt():
    s = random.randint(0, 1000)
    s = str(s)
    salt = '0000'
    return salt[:len(salt)-len(s)]+s


# img = Image.new('RGBA', (100, 100), (255, 0, 0, 0)) transparent

def generate_images(amount_of_images=1, side_size=100):

    img = Image.new('RGBA', (side_size, side_size), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    for j in range(0, amount_of_images):

        for i in range(0, random.randint(1, side_size*side_size/2)):
            
            if random.randint(1, 27) % 27 == 0:
                c = random.randint(0, side_size-1)
                coords = (c, c)
            else:
                coords = tuple(random.sample(range(0, side_size), 2))
            
            if random.randint(1, 4) % 2 == 0:
                img.putpixel(coords, (0, 0, 0))
            else:
                img.putpixel(coords, (255, 255, 255))

        img.save(f'DATA/sqr_{get_salt()}.png', 'PNG')
    

def create_img_from_np_arr(np_arr):
    pass


def open_sample_image():
    pass


generate_images(6, 200)

