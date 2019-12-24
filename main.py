import os
from datetime import datetime
from inky import InkyPHAT
from PIL import Image, ImageDraw

inky_display = InkyPHAT('black')

imgs_dir = "/home/pi/lyrics-frame/images"

imgs = [os.path.join(imgs_dir, f) for f in os.listdir(imgs_dir) if os.path.isfile(os.path.join(imgs_dir, f))]

day_of_year = datetime.now()

img_of_the_day = day_of_year % len(imgs)

img = Image.open(imgs[img_of_the_day])

inky_display.set_image(img)
inky_display.show()
