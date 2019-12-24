import os
import logging
from datetime import datetime
from inky import InkyPHAT
from PIL import Image, ImageDraw

# logging config
logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

inky_display = InkyPHAT('black')

# gets all images in the images dir
imgs_dir = "/home/pi/lyrics-frame/images"
imgs = [os.path.join(imgs_dir, f) for f in os.listdir(imgs_dir) if os.path.isfile(os.path.join(imgs_dir, f))]

logging.info({"imgs": imgs})

# take a day to get the image of the day
day_of_year = datetime.now().timetuple().tm_yday - 1
img_of_the_day = day_of_year % len(imgs)
img_file = imgs[img_of_the_day]
logging.info({"day_of_year": day_of_year, "img_of_the_day": img_of_the_day, "img_file": img_file})

img = Image.open(img_file)

# interfaces with inky to set the image in the display
inky_display.set_image(img)
inky_display.show()
