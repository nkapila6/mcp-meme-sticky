#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2025-05-19 12:41:56 Monday

@author: Nikhil Kapila
"""

# Pickle convert to .Py
# Was used as a preprocessing step, not used in the mcp server.

import pickle
import pprint


def convert(path:str):
    with open(path, 'rb') as f:
        templates_dict = pickle.load(f)

    with open('templates_dict.py', 'w') as f:
        f.write("# Templates dictionary converted from pickle\n\n")
        f.write("templates = ")
        f.write(pprint.pformat(templates_dict, indent=4))
        f.write("\n")

    print("Conversion complete. Check templates_dict.py")