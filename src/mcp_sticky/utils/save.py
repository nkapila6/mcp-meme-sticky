#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2025-05-18 23:22:33 Sunday

@author: Nikhil Kapila
"""

# Meme saving utility. Weee.

import os, requests
import webbrowser

from pathlib import Path
from typing import Optional
from .fetch import fetch_tele_link

PATH = os.path.join(Path.home(), "Desktop")

def saver(meme_link:str,
          save_on_desktop:bool,
          return_tele_sticker:bool)->str:

    response:str = ""
    
    if save_on_desktop: 
        path:str = save_image(meme_link)
        webbrowser.open(meme_link, new=1, autoraise=True)
        response += f'Image saved at {path}. '

    if return_tele_sticker:
        tg_link = fetch_tele_link(meme_link)
        webbrowser.open(tg_link, new=1, autoraise=True)
        response += f'Opening telegram bot at f{tg_link}'

    return response

def save_image(url:str, path:Optional[str]=None)->str:
    """Saves image to Desktop.

    Args:
        url (str): Takes incoming URL, downloads it and saves it to the desktop.
        path (str, default None): If user wants to specify a path, they can.
    Returns:
        str: Returns output path of saved image.
    """

    filename = "meme_image.png"
    OUT_PATH = os.path.join(PATH, filename)

    response = requests.get(url)
    if response.status_code == 200:
        # Write the image data to a file on the desktop
        with open(OUT_PATH, "wb") as f:
            f.write(response.content)
        print(f"Image successfully saved to {OUT_PATH}")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

    return OUT_PATH