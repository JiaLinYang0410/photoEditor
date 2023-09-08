from PIL import Image, ImageEnhancer, ImageFilter
import os

#folder with photos to be edited
path = './imgs'
#folder where edited photos go
pathOut = '/editedImgs'

#access all the photos in the folder
for file in os.listdir(path):
    #opening the image
    img = Image.open(f"{path}/{filename}")
