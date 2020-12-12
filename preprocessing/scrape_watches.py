
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


#base_path =  "/home/kalyani/Documents/Fall_20/CSE 599_DL/GANS/Watches/"
#base_path_output = "/home/kalyani/Documents/Fall_20/CSE 599_DL/GANS/output_Watches/"
#base_path_final = "/home/kalyani/Documents/Fall_20/CSE 599_DL/GANS/final_Watches/"

base_path = '../DiscoGAN/datasets/'
path_edges2watches = base_path + 'edges2watches/' #f'{base_path}/edges2watches/'
path_watches = base_path + 'watches/' #f'{base_path}/watches/'
path_watches_edges = base_path + 'watches_edges/' #f'{base_path}/watches_edges/'

#Create directory's if they dont exist
if not os.path.exists(base_path):
    print("Base path does not exist.")
    exit(1)

if not os.path.exists(path_edges2watches):
    os.makedirs(path_edges2watches)
    #os.makedirs(f'{path_edges2watches}train')
    #os.makedirs(f'{path_edges2watches}val')
    os.makedirs(path_edges2watches + 'train')
    os.makedirs(path_edges2watches + 'val')

if not os.path.exists(path_watches):
    os.makedirs(path_watches)

if not os.path.exists(path_watches_edges):
    os.makedirs(path_watches_edges)


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
        urllib.request.urlretrieve(img_url, path_watches + filename)
        im_png = Image.open(path_watches + filename ).convert("RGBA")
        new_image = Image.new("RGBA", im_png.size, "WHITE")  # Create a white rgba background
        new_image.paste(im_png, (0, 0),
                        im_png)  # Paste the image on the background. Go to the links given below for details.
        new_image.convert('RGB').save( path_watches + filename, "PNG")  # Save as PNG

        resized_image = new_image.resize((128, 128))
        resized_image.save(path_watches + filename )
        #img = PImage.open(path_watches + image)
        #edgeDetector.preprocess(path_watches, path_watches_edges)

        imagelist.append(image)
        if idx ==100:
            break


#
#
# imagesList = listdir(path_watches)
# loadedImages = []
# for image in imagesList:
#     img = PImage.open(path_watches + image)
#     edgeDetector.preprocess(path_watches, path_watches_edges)
#
#
edgeDetector.preprocess(path_watches, path_watches_edges)

imagesList = listdir(path_watches)
for image in imagesList:
    print(image)
    # img1 = cv2.imread(str(path_watches) + str(image))
    # img2 = cv2.imread(str(path_watches) + str(image))
    # vis = np.concatenate((img1, img2), axis=1)
    # cv2.imwrite(str(path_edges2watches) + str(image), vis)

    images = [Image.open(x) for x in [ str(path_watches_edges) + str(image), str(path_watches) + str(image)]]
    total_width = 256
    max_height = 128

    final_im = Image.new('RGB', (total_width, max_height), (255, 255, 255, 255))

    x_offset = 0
    for im in images:
        final_im.paste(im, (x_offset, 0))
        x_offset += im.size[0]

    final_im.save(str(path_edges2watches) + str(image))