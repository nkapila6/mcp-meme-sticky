#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2025-05-18 23:20:31 Sunday

@author: Nikhil Kapila
"""

# URL creation and fetching utils
import pickle
from .crawlers.google import GoogleCrawler

TELEGRAM_BOT_URL = "https://t.me/mcp_sticky_bot?text="
MEMEGEN_CUSTOM_URL = "https://api.memegen.link/images/custom/_/{text}.png?background={url}"

def fetch_resource(path:str)->dict:
    """Fetches a pickled object at specified path.

    Args:
        path (str): Pickled object.

    Returns:
        dict: fetched dict.
    """

    with open(path, 'rb') as f:
        return pickle.load(f)

def fetch_image_url(search_query:str)->str:
    """Fetch Image URL.

    Args:
        search_query (str): Crawls Google to fetch an image URL for downstream meme making :).
        
    Returns:
        str: Returns first link from list of links. This is normally the most accurate.
    """
    # TODO: The Crawler has capabilities to do GIF search but this still needs an implementation in the Telegram bot.
    url = GoogleCrawler(search_query)[0]
    return url

def make_meme_custom(url:str, meme_text:str)->str:
    """Makes custom meme using memegen.link.
    https://memegen.link/

    Args:
        url (str): Background image link.
        meme_text (str): Generated meme text through creative "LLM".

    Returns:
        str: returns URL.
    """
    return MEMEGEN_CUSTOM_URL.format(text=meme_text,
                              url=url)

def make_meme_from_template(url:str, meme_text:list)->str:
    """Make meme using memegen templates.

    Args:
        url (str): Memegen URL from db.
        meme_text (list): A list of texts for the template.

    Returns:
        str: Memegen link.
    """
    # getting rid of .jpg
    
    url = url[:-4]
    for i in meme_text:
        url = f'{url}/{i}'
    url = f'{url}.jpg'
    return url

def fetch_tele_link(url:str)->str:
    """Makes Telegram Link to MCP Sticky Bot to create Sticker.

    Args:
        url (str): Incoming meme URL link.

    Returns:
        str: Outgoing bot init link.
    """
    return TELEGRAM_BOT_URL+url