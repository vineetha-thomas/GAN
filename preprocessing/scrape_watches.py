
from bs4 import BeautifulSoup
import requests
import urllib.request
import shutil

import urllib
from PIL import Image
import os
import edgeDetector
from os import listdir
from PIL import Image as PImage
import cv2
import numpy as np



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
}


base_path =  "/home/kalyani/Documents/Fall_20/CSE 599_DL/GANS/Watches/"
base_path_output = "/home/kalyani/Documents/Fall_20/CSE 599_DL/GANS/output_Watches/"
base_path_final = "/home/kalyani/Documents/Fall_20/CSE 599_DL/GANS/final_Watches/"

imagelist = []
idx = 0
for page in range(5):
    url = "https://www.watchdetails.com/page/"+str(page)+"/"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    images = soup.find_all("img","entry-thumb")


    for image in images:
        idx+=1
        #print(type(image))
        #print(image)
        img_url = image.get('data-img-url')
        #print(img_url)
        #filename=img_url.split('/')[-1]
        #print(filename)
        filename = str(idx) +'.png'
        urllib.request.urlretrieve(img_url, base_path + filename)
        im_png = Image.open(base_path + filename ).convert("RGBA")
        new_image = Image.new("RGBA", im_png.size, "WHITE")  # Create a white rgba background
        new_image.paste(im_png, (0, 0),
                        im_png)  # Paste the image on the background. Go to the links given below for details.
        new_image.convert('RGB').save( base_path + filename, "PNG")  # Save as PNG

        resized_image = new_image.resize((128, 128))
        resized_image.save(base_path + filename )
        #img = PImage.open(base_path + image)
        #edgeDetector.preprocess(base_path, base_path_output)

        imagelist.append(image)
        if idx ==100:
            break


#
#
# imagesList = listdir(base_path)
# loadedImages = []
# for image in imagesList:
#     img = PImage.open(base_path + image)
#     edgeDetector.preprocess(base_path, base_path_output)
#
#
edgeDetector.preprocess(base_path, base_path_output)

imagesList = listdir(base_path)
for image in imagesList:
    print(image)
    # img1 = cv2.imread(str(base_path) + str(image))
    # img2 = cv2.imread(str(base_path_output) + str(image))
    # vis = np.concatenate((img1, img2), axis=1)
    # cv2.imwrite(str(base_path_final) + str(image), vis)

    images = [Image.open(x) for x in [ str(base_path_output) + str(image), str(base_path) + str(image)]]
    total_width = 256
    max_height = 128

    final_im = Image.new('RGB', (total_width, max_height), (255, 255, 255, 255))

    x_offset = 0
    for im in images:
        final_im.paste(im, (x_offset, 0))
        x_offset += im.size[0]

    final_im.save(str(base_path_final) + str(image))