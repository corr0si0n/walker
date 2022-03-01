from random import randint
from math import floor

from progressbar import progressbar
from PIL import Image, ImageDraw

width, height = (1000, 1000)
spacing = 10
padding = 1
cols = round(width / spacing)
rows = round(height / spacing)
x, y = (int(cols / 2), int(rows / 2))

grid = [[col for col in range(cols)] for row in range(rows)]

image = Image.new('RGB', (width, height), (0, 0, 0, 0))
draw = ImageDraw.Draw(image, 'RGBA')
color = (255, 255, 255, 25)
radius = spacing / 2


def draw_point(x, y):
    draw.ellipse(
        [(x * spacing - radius + padding, y * spacing - radius + padding),
         (x * spacing + radius - padding, y * spacing + radius - padding)],
        fill=color)


for step in progressbar(range(width * height)):
    draw_point(x, y)
    direction = randint(0, 3)
    if direction == 0:
        x = x + 1
    elif direction == 1:
        x = x - 1
    elif direction == 2:
        y = y + 1
    else:
        y = y - 1

image.show()