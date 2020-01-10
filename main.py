import re
import requests
import urllib.request
import time
import os
from bs4 import BeautifulSoup

def main(keyword):
    page = requests.get(f"https://tenor.com/search/{keyword}-gifs")
    soup = BeautifulSoup(page.content, 'html.parser')
    # for img in soup.find_all("img"):
    #     if (re.search(".gif$", img)):
    #         print(img['src'])
    urls = [img['src'] for img in soup.find_all('img', src=re.compile('\Ahttps://media.tenor.com'))]
    i = 0
    if not os.path.exists("output"):
        os.makedirs("output")
    for url in urls:
        if not os.path.exists(f"./output/{keyword}"):
            os.makedirs(f"./output/{keyword}")
        urllib.request.urlretrieve(url, f'./output/{keyword}/{keyword}_{i}')
        print(url)
        i += 1
        time.sleep(1)

if __name__ == "__main__":
    main("passionate-kiss")