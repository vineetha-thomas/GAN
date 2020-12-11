
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
#base_path =  "/home/kalyani/Documents/Fall_20/CSE 599_DL/GANS/Tshirts/"
#base_path_output =  "/home/kalyani/Documents/Fall_20/CSE 599_DL/GANS/output_Tshirts/"
#base_path_final = "/home/kalyani/Documents/Fall_20/CSE 599_DL/GANS/final_Tshirts/"

base_path = '../DiscoGAN/datasets/'
path_edges2tshirts = f'{base_path}/edges2tshirts/'
path_tshirts = f'{base_path}/tshirts/'
path_tshirts_edges = f'{base_path}/tshirts_edges/'

#Create directory's if they dont exist
if not os.path.exists(base_path):
    print("Base path does not exist.")
    exit(1)

if not os.path.exists(path_edges2tshirts):
    os.makedirs(path_edges2tshirts)
    os.makedirs(f'{path_edges2tshirts}train')
    os.makedirs(f'{path_edges2tshirts}val')

if not os.path.exists(path_tshirts):
    os.makedirs(path_tshirts)

if not os.path.exists(path_tshirts_edges):
    os.makedirs(path_tshirts_edges)


imagelist = []
idx = 0
for page in range(1, 36):
    url = "https://fineartamerica.com/shop/womens+tshirts/zoro?page="+str(page)
    print(url)
    response = requests.get(url, headers=headers)
    #print(response)
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup)
    images = soup.find_all("img")
    #print(images)


    for image in images:
        #print(type(image))
        #print(image)
        #print(idx)
        if idx == 100:
            break

        try:
            img_url = image.get('data-src')
            #print(img_url)
            filename=img_url.split('/')[-1]
            filename = str(idx)
            urllib.request.urlretrieve(img_url, path_tshirts + filename +'.jpg')

            im_jpg = Image.open(path_tshirts + filename +'.jpg')
            resized_image = im_jpg.resize((128, 128))
            resized_image.save(path_tshirts + filename +'.png')
            os.remove(path_tshirts + filename +'.jpg')
            #print(filename)
            idx= idx+1

        except:
            pass

        #
        # imagelist.append(image)

num_images = idx
edgeDetector.preprocess(path_tshirts, path_tshirts_edges)

# imagesList = listdir(path_tshirts)
# loadedImages = []
# for image in imagesList:
#     img = PImage.open(path_tshirts + image)

#train-val split
val_size = int(num_images*0.1)
val_idx = np.random.choice(num_images, val_size)

imagesList = listdir(path_tshirts)
idx=0
for image in imagesList:
    #print(image)
    # img1 = cv2.imread(str(path_tshirts) + str(image))
    # img2 = cv2.imread(str(path_tshirts_edges) + str(image))
    # vis = np.concatenate((img1, img2), axis=1)
    # cv2.imwrite(str(path_edges2tshirts) + str(image), vis)
    idx = idx+1
    images = [Image.open(x) for x in [ str(path_tshirts_edges) + str(image), str(path_tshirts) + str(image)]]
    total_width = 256
    max_height = 128

    final_im = Image.new('RGB', (total_width, max_height), (255, 255, 255, 255))

    x_offset = 0
    for im in images:
        final_im.paste(im, (x_offset, 0))
        x_offset += im.size[0]

    if idx in val_idx:
        #final_im.save(str(path_edges2tshirts) + str(image))
        final_im.save(f'{path_edges2tshirts}/val/{image}')
    else:
        final_im.save(f'{path_edges2tshirts}/train/{image}')
