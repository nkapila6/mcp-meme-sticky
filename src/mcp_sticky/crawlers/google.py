#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2025-05-18 14:52:51 Sunday

@author: Nikhil Kapila
"""

import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode

# inspired from icrawler library:
#   parser.py: https://github.com/hellock/icrawler/blob/598dd4329a7db9695ac9d77e557622bbb831ce49/icrawler/parser.py
#   google.py: https://github.com/hellock/icrawler/blob/598dd4329a7db9695ac9d77e557622bbb831ce49/icrawler/builtin/google.py

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.google.com/',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0',
    }

def GoogleFeeder(keyword:str, return_gif)->tuple:
        base_url = 'https://www.google.com/search?'
        # keyword = keyword+' meme template' --> will let llm decide query
        # size pegged to 512,512
        params = dict(q=keyword, ijn=0, start=0, tbs='isz:ex,iszw:512,iszh:512', tbm='isch')
        if return_gif:
            # for gifs
            params['tbs'] = 'itp:animated'
        print(f'Search query is {keyword}.')
        url = base_url + urlencode(params)
        return url, base_url, params

def GoogleParser(base_url, params, return_gif)->list:
    session = requests.Session()
    session.headers.update(headers)
    re1 = r"http[^\[]*?.(?:jpg|png|bmp)" if not return_gif else r"http[^\[]*?.(?:gif)"
    re2 = r"http[^\[]*?\.(?:jpg|png|bmp)" if not return_gif else r"http[^\[]*?\.(?:gif)"

    response = session.get(
                base_url, 
                params=params, 
                # proxies=proxies, 
                timeout=10
            )

    soup = BeautifulSoup(response.content, 'html.parser')
    image_divs = soup.find_all(name="script")
    bgs = []
    for div in image_divs:
            txt = str(div)
            uris = re.findall(re1, txt)
            if not uris:
                uris = re.findall(re2, txt)
            uris = [bytes(uri, "utf-8").decode("unicode-escape") for uri in uris]
            if uris:
                # print(div)
                # return uris, [{"file_url": uri} for uri in uris]
                bgs.extend(uris)
    return bgs

def is_image_url_valid(url, timeout=5):
    try:
        response = requests.head(url, timeout=timeout)
        if response.status_code == 200:
            content_type = response.headers.get('Content-Type', '')
            if 'image' in content_type:
                return True
        return False
    except requests.exceptions.RequestException:
        return False
        
def GoogleCrawler(keyword:str, return_gif:bool=False)->list:
    url, base_url, params = GoogleFeeder(keyword, return_gif)
    print(f'Search URL is {url} with params {params}.')
    backgrounds = GoogleParser(base_url, params, return_gif)
    # take only first 10
    bgs = backgrounds[:10]
    bgs = [url for url in bgs if not any(x in url for x in [
        'istockphoto', 
        'redd', 
        'google.com/search', 
        'cdn-icons-png', 
        'hiclipart',
        'makeagif', 
        'pinterest'
    ]) and url != 'https://png']
    bgs = [url for url in bgs if is_image_url_valid(url)]
    return bgs