import re
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

def main(keyword):
    page = requests.get("https://tenor.com/search/{keyword}-gifs")
    soup = BeautifulSoup(page.content, 'html.parser')
    urls = [img['src'] for img in soup.find_all('img', src=re.compile('.gif\Z'))]
    for url in urls:
        print(url)

if __name__ == "__main__":
    main("crying")