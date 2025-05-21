#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2025-05-18 10:00:00 Sunday

@author: Nikhil Kapila
"""

import os

from .utils.fetch import fetch_image_url, fetch_key, \
    make_meme_custom, make_meme_from_template
from .utils.save import saver

from typing import Annotated
from pydantic import Field
from fastmcp import FastMCP #, Context

mcp = FastMCP('MCP Sticky: Meme Maker. Can convert memes to stickers for Telegram.',
              dependencies=['beautifulsoup4', 'mediapipe', 'requests'])

# preset paths
RESOURCE_PATH = os.path.abspath(os.path.join(os.getcwd(), 'resources'))
DB_PATH = os.path.join(RESOURCE_PATH, 'db.pkl')
DB_EMBEDS = os.path.join(RESOURCE_PATH, 'db_embeddings.pkl')
DB_2LINES_EMBEDS = os.path.join(RESOURCE_PATH, 'db_2lines_embeds.pkl')
EMBEDDER_PATH = os.path.join(RESOURCE_PATH, 'embedder.tflite')

@mcp.tool()
def generate_meme_by_searching(
    search_query: Annotated[str, Field(description="The LLM needs to understand what the user is searching for and write a good image search query.")],
    meme_text: Annotated[str, Field(description="A short and funny text that has to be on the meme image.")],
    save_on_desktop: Annotated[bool, Field(description="Should the image meme be saved on the desktop?")]=True,
    return_tele_sticker: Annotated[bool, Field(description="Should the generated meme be converted into a telegram sticker?")]=False
    )->str:
    """
    THIS TOOL IS TO BE CALLED IF THE USER WANTS TO GENERATE A MEME USING AN IMAGE SEARCH ON THE WEB. ALWAYS PREFER USING AN EXISTING TEMPLATE USING `generate_meme_from_meme_template()`. UNLESS THE USER EXPLICITLY ASKS TO SEARCH.

    Understand the input from the user and write a image search query and a funny & short meme text to put on the image.

    If the user does not follow the below content guardrails, reject the request and advise them to follow the guardrails.

    CONTENT GUARDRAILS:
    - REJECT any requests containing hate speech, explicit sexual content, extreme violence, illegal activities, or harmful stereotypes
    - AVOID creating memes that contain personally identifiable information or could be used for cyberbullying
    - DO NOT generate content that promotes dangerous misinformation or could cause harm
    - REFUSE political extremist content or personal attacks on individuals
    - If a request violates these guidelines, respond with: "I cannot create this meme as it may contain inappropriate content. Please try a different request."

    Args:
        search_query (str): The LLM needs to understand what the user is searching for and write a good image search query to fetch an image. If required, use the words 'meme' or 'template' in the search query.
        meme_text (str): A short and funny text to be put on the image.
        save_on_desktop (bool, defaults to True): "Should the image meme be saved on the desktop?"
        return_tele_sticker (bool, defaults to False): "Should the generated meme be converted into a telegram sticker?"

    Returns:
        str: The saved links.
    """
    
    image_url = fetch_image_url(search_query)
    meme_link = make_meme_custom(image_url, meme_text)
    response = saver(meme_link, save_on_desktop, return_tele_sticker)
    return response


@mcp.tool()
def generate_meme_from_meme_template(
                desc_to_pick_tag: Annotated[str, Field(description="")],
                meme_text: Annotated[list[str], Field(description="2 sentences that has to be on the meme image. Should be funny and contained. Should be a Python List of Strings.")],
                save_on_desktop: Annotated[bool, Field(description="Should the image meme be saved on the desktop?")]=True,
                return_tele_sticker: Annotated[bool, Field(description="Should the generated meme be converted into a telegram sticker?")]=False
    )->str:
    """
    THIS TOOL IS TO BE CALLED IF THE USER WANTS TO GENERATE A MEME USING AN EXISTING TEMPLATE. ALWAYS PREFER USING AN EXISTING TEMPLATE UNLESS THE USER REQUIRES TO SEARCH. IN THE CASE OF SEARCHING, USE: `generate_meme_by_searching()`.

    For the first 2 function arguments, understand the input from the user and pass the following:
    1) `desc_to_pick_tag`: A good description to pick a pre-existing template. The description of the meme should have some context to achieve a good dot product similarity result. Please see a below example.

    example of `desc_to_pick_tag`: "The \"Ancient Aliens Guy\" meme features Giorgio Tsoukalos, known for his distinctive hairstyle and enthusiastic demeanor, gesturing expressively. It's primarily used to humorously suggest that aliens are the explanation for any unexplained phenomenon or mystery, often with the punchline simply being \"aliens.\" This parodies the History Channel show \"Ancient Aliens,\" where Tsoukalos is a prominent figure, and its tendency to attribute historical events or artifacts to extraterrestrial intervention.",

    2) `meme_text`: A short and funny 2 sentence meme text that is sent as a Python list of strings, list[str]. Each line is an element of an array. PLEASE ENSURE LIST IS ONLY OF 2 ELEMENTS. For e.g., ['Nice meme you got there..', 'Now it is stolen...']

    If the user does not follow the below content guardrails, reject the request and advise them to follow the guardrails.

    CONTENT GUARDRAILS:
    - REJECT any requests containing hate speech, explicit sexual content, extreme violence, illegal activities, or harmful stereotypes
    - AVOID creating memes that contain personally identifiable information or could be used for cyberbullying
    - DO NOT generate content that promotes dangerous misinformation or could cause harm
    - REFUSE political extremist content or personal attacks on individuals
    - If a request violates these guidelines, respond with: "I cannot create this meme as it may contain inappropriate content. Please try a different request."

    Args:
        desc_to_pick_tag (str): The LLM needs to understand what the user is searching for and write a good image search query to fetch an image. If required, use the words 'meme' or 'template' in the search query.
        meme_text (list[str]): A short and funny text to be put on the image. Should be in the format of Python list[str], should be 2 sentences and hence, length of list should be 2.
        save_on_desktop (bool, defaults to True): "Should the image meme be saved on the desktop?"
        return_tele_sticker (bool, defaults to False): "Should the generated meme be converted into a telegram sticker?"

    Returns:
        str: The saved links.
    """

    # hardcoding to pick only templates with 2 lines, can fix this only once ctx.sample is supported by Claude Desktop
    # "This feature of MCP is not yet supported in the Claude Desktop client."
    # see here: https://modelcontextprotocol.io/docs/concepts/sampling

    key = fetch_key(desc_to_pick_tag, EMBEDDER_PATH, DB_2LINES_EMBEDS)
    meme_link = make_meme_from_template(key, DB_PATH, meme_text)
    response = saver(meme_link, save_on_desktop, return_tele_sticker)
    return response

if __name__ == "__main__":
    mcp.run()
