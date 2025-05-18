#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2025-05-18 23:22:33 Sunday

@author: Nikhil Kapila
"""

# Meme saving utility. Weee.

import os
import requests
from pathlib import Path
from typing import Optional

PATH = os.path.join(Path.home(), "Desktop")

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