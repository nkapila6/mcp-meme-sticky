#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2025-05-18 10:00:00 Sunday

@author: Nikhil Kapila
"""

from fastmcp import FastMCP, Context
from fastmcp.prompts.prompt import Message

from utils.fetch import fetch_image_url, fetch_tele_link, make_meme
from utils.save import save_image

mcp = FastMCP('Sticker Maker for WhatsApp and Telegram', 
              dependencies=['beautifulsoup4', 'requests'])

# for preset meme templates
MEMEGEN_URL_PRESET = ""

@mcp.tool()
async def parse_message(message:str, ctx:Context)->tuple:
    """
    THIS TOOL IS TO BE CALLED FIRST AND IS TO PROVIDE ADDITIONAL CONTEXT to the next tool `generate_meme()`.

    Generates a meme or sticker based on the users request. 
    Analyze the incoming message, extract relevant search terms and generate meme text.
    Reply with the following:
    1. What should I search for on Google Search to find an appropriate image? Give a clear search query.
    2. What text should be placed on the meme? 

    Format the message as:
    SEARCH: [search query]
    TEXT: [meme text]

    The output of this tool goes to the next tool `generate_meme()`.

    Args:
        message (str): Input query to make meme
        ctx (Context): Incoming context.

    Returns:
        Nothing, the LLM just constructs the output for `generate_meme()`.
    """
    await ctx.info('Parsing input message...')
    print(message)
    
@mcp.tool()
async def generate_meme(message:str,
                        ctx:Context,
                        want_tele_sticker:bool=False,
                        save_as_image:bool=True)->str:
    """Generate memes. 
    Takes the input from the previous `parse_message` tool and allows the user to gnerate memes.

    Args:
        message (str): Input message from `parse_message`.
        ctx (Context): Incoming context.
        want_tele_sticker (bool, default=False): If the user wants a Telegram sticker.
        save_as_image (bool, default=True): Saves the image to the users desktop.

    Returns:
       meme_link (str, default): the generated meme link.
       tele_link (if want_tele_sticker=True): returns Telegram sticker.
       
    """
    await ctx.info('Stripping out search terms and meme text.')
    lines = message.strip().split('\n')
    search_query, meme_text = "", ""

    for line in lines:
        if line.startswith('SEARCH'):
            search_query = line.replace('SEARCH: ', '').strip()
        elif line.startswith('TEXT'):
            meme_text = line.replace('TEXT: ', '').strip()

    url = fetch_image_url(search_query)
    meme_link = make_meme(url, meme_text)

    if save_as_image: save_image(meme_link)

    if want_tele_sticker:  return fetch_tele_link(meme_link)

    return meme_link


# CLAUDE DESKTOP does not support MCP Sampling so approaching the problem differently.
# https://modelcontextprotocol.io/docs/concepts/sampling
# Using nested tool calling in the meantime 
#   (this is playing with fire at the moment (this whole MCP USB-C shit is fire anyway) until I find a better solution).
# async def parse_message(message:str, ctx:Context)->tuple:
#     await ctx.debug('Parsing input query by user.')

#     prompt=f"""
#     Analyze the message requesting a meme: "{message}"
#     Reply with the following:
#     1. What should I search for on Google Search to find an appropriate image? Give a clear search query.
#     2. What text should be placed on the meme? 

#     Format your response as:
#     SEARCH: [search query]
#     TEXT: [meme text]
#     """
#     response = await ctx.sample(messages=prompt)
#     await ctx.debug(f'Context sample returns response: {response}')

#     lines = response.text.strip().split('\n')
#     await ctx.debug(f'The lines stripped are {lines}.')

#     for line in lines:
#         if line.startswith('SEARCH'):
#             search_query = line.replace('SEARCH: ', '').strip()
#         elif line.startswith('TEXT'):
#             meme_text = line.replace('TEXT: ', '').strip()

#     return response


if __name__ == "__main__":
    mcp.run()
