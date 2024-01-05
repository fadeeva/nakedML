import random

from PIL import Image, ImageDraw


def get_salt():
    s = random.randint(0, 1000)
    s = str(s)
    salt = '0000'
    return salt[:len(salt)-len(s)]+s


# img = Image.new('RGBA', (100, 100), (255, 0, 0, 0)) transparent

img = Image.new('RGBA', (100, 100), (255, 255, 255))
draw = ImageDraw.Draw(img)

for j in range(0, 10):

    for i in range(0, random.randint(1, 10000)):
        coords = tuple(random.sample(range(0, 100), 2))
        img.putpixel(coords, (0, 0, 0))

    img.save(f'DATA/sqr_{get_salt()}.png', 'PNG')
    
    