from inky import InkyPHAT
from PIL import Image, ImageDraw

inky_display = InkyPHAT('black')

img = Image.open('./images/deixaeulheconvencer.png')

inky_display.set_image(img)
inky_display.show()
