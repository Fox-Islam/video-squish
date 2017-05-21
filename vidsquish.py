import cv2
import numpy as np
import colorsys
import imageio
import sys
import os
from PIL import Image

def generate_pic (i,colours, size):
    height = size[1]
    img = np.zeros((height,len(colours),3), np.uint8)
    for x in range(0, len(colours)):
        for y in range(0, height):
            img[y,x,:] = colours[x][y,0]
    img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
    cv2.imwrite("vidsquish_%d.png" % i, img)
    img = Image.open('vidsquish_' + str(i) + '.png')
    new_im.paste(img, (i,0))
    img.close()
    os.remove('vidsquish_' + str(i) + '.png')

def resize_image (image, size=200):
    h, w, _ = image.shape
    w_new = int(size * w / max(w, h) )
    h_new = int(size * h / max(w, h) )
    image = cv2.resize(image, (w_new, h_new));
    return image

def process_frame (frame, height=200):
    image = resize_image(frame)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    image = image.reshape((image.shape[0] * image.shape[1], 1, 3))
    image_column = cv2.resize(image, (1, height), interpolation=cv2.INTER_AREA)
    return image_column

def process_video (input_movie, size=(2000,200)): 
    colours = []
    colours_frame = process_frame(input_movie, size[1])
    colours.append(colours_frame)
    generate_pic(i,colours, size)
    if i % 100 == 0: # Measuring progress for peace of mind or something
        print(i)

#imageio.plugins.ffmpeg.download() # Uncomment this if ffmpeg is not installed

path = raw_input('Path? ') # Ex.: "C:\Users\Me\Downloads\video"
savename = raw_input('Output name? ') # Name of the output image
input_movie = imageio.get_reader(path + '.mp4','ffmpeg')

frames = int(input_movie.get_meta_data()['duration'])
fps = int(input_movie.get_meta_data()['fps'])
width = frames * fps #Final image width
new_im = Image.new('RGB', (width, 200)) #Initialising final image

for i, im in enumerate(input_movie):
    process_video(input_movie.get_data(i),(width,200))
    if i == width:
        break
new_im.save(savename + '.png')

