#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2025-05-18 23:20:31 Sunday

@author: Nikhil Kapila
"""

# URL creation and fetching utils
import pickle
from .crawlers.google import GoogleCrawler

from mediapipe.tasks import python
from mediapipe.tasks.python import text

TELEGRAM_BOT_URL = "https://t.me/mcp_sticky_bot?text="
MEMEGEN_CUSTOM_URL = "https://api.memegen.link/images/custom/_/{text}.png?background={url}"

def fetch_embedder(path:str, l2_normalize:bool=True, quantize:bool=True):# ->text.text_embedder.TextEmbedder:
    base_options = python.BaseOptions(model_asset_path=path)
    l2_normalize, quantize = True, True
    options = text.TextEmbedderOptions(
        base_options=base_options, l2_normalize=l2_normalize, quantize=quantize)
    embedder = text.TextEmbedder.create_from_options(options)
    return embedder

def fetch_key(query:str, embedder_path:str, embedding_db_path:str)->str:
    """Fetch a key from the meme template.

    Args:
        query (str): Description/Context of meme from MCP host.
        embedder_path (str): Path of embedder.
        embedding_db_path (str): Path of embedding db.

    Returns:
        str: Key in embedding db.
    """
    embedder = fetch_embedder(embedder_path)
    embedding_db = fetch_resource(embedding_db_path)
    query_embedding = embedder.embed(query).embeddings[0]

    scores = {}
    for k,template_embedding in embedding_db.items():
        scores[k] = text.TextEmbedder.cosine_similarity(
                        template_embedding, query_embedding)

    filter_scores = {k:v for k,v in scores.items() if v>0.95}

    if len(filter_scores)>0: # if length of filter scores is>0 then pick one
        return pick_random_key(list(filter_scores.keys()))
    else: # if filter scores has no match then lower threshold and check
        filter_scores = {k:v for k,v in scores.items() if v>0.80}
        if len(filter_scores)>0: return pick_random_key(list(filter_scores.keys()))
        else: return pick_random_key(list(scores.keys())) 
        
def pick_random_key(keys:list)->str:
    """Pick random key.

    Args:
        keys (list): List of keys.

    Returns:
        str: Chosen random key.
    """
    import random
    return random.choice(keys)
    

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

def make_meme_from_template(key:str, DB_PATH:str, meme_text:list[str])->str:
    """Make meme using memegen templates.

    Args:
        url (str): Memegen URL from db.
        meme_text (list): A list of texts for the template.

    Returns:
        str: Memegen link.
    """

    db = fetch_resource(DB_PATH)
    url = db[key]['blank']
    url = url[:-4] # getting rid of .jpg
    
    for sent in meme_text:
        url = f'{url}/{sent}'
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