
from bs4 import BeautifulSoup
import requests
import urllib.request
import shutil

import urllib


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
base_path =  "/home/kalyani/Documents/Fall_20/CSE 599_DL/GANS/Watches/"
imagelist = []
for page in range(1):
    url = "https://www.watchdetails.com/page/"+str(page)+"/"
    response = requests.get(url, headers=headers)
    print(response)
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup)
    images = soup.find_all("img","entry-thumb")

    for image in images:
        print(type(image))
        print(image)
        img_url = image.get('data-img-url')
        print(img_url)
        filename=img_url.split('/')[-1]
        urllib.request.urlretrieve(img_url, base_path + filename)

        imagelist.append(image)


