
from bs4 import BeautifulSoup
import requests
import urllib.request
import shutil

import urllib
import time
import PIL
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

#
# url =  "https://www.amazon.com/watches/s?k=watches"
# url= "https://www.watchdetails.com/page/3/"
# response = requests.get(url, headers= headers)
# print(response)
# soup = BeautifulSoup(response.text, "html.parser")
# #print(soup)
# images = soup.find_all("img")
# print(images)
import time
base_path =  "/home/kalyani/Documents/Fall_20/CSE 599_DL/GANS/Tshirts/"
base_path_output =  "/home/kalyani/Documents/Fall_20/CSE 599_DL/GANS/output_Tshirts/"
base_path_final = "/home/kalyani/Documents/Fall_20/CSE 599_DL/GANS/final_Tshirts/"

imagelist = []
idx = 0
for page in range(1, 36):
    url = "https://fineartamerica.com/shop/womens+tshirts/zoro?page="+str(page)
    print(url)
    response = requests.get(url, headers=headers)
    print(response)
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup)
    images = soup.find_all("img")
    print(images)


    for image in images:
        #print(type(image))
        #print(image)
        print(idx)
        if idx == 100:
            break

        try:
            img_url = image.get('data-src')
            #print(img_url)
            filename=img_url.split('/')[-1]
            filename = str(idx)
            urllib.request.urlretrieve(img_url, base_path + filename +'.jpg')

            im_jpg = Image.open(base_path + filename +'.jpg')
            resized_image = im_jpg.resize((128, 128))
            resized_image.save(base_path + filename +'.png')
            os.remove(base_path + filename +'.jpg')
            #print(filename)



            idx= idx+1

        except:
            pass

        #
        # imagelist.append(image)

edgeDetector.preprocess(base_path, base_path_output)

# imagesList = listdir(base_path)
# loadedImages = []
# for image in imagesList:
#     img = PImage.open(base_path + image)



imagesList = listdir(base_path)
for image in imagesList:
    #print(image)
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