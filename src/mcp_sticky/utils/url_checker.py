#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2025-05-19 14:36:26 Monday

@author: Nikhil Kapila
"""

from urllib.parse import urlparse

def is_url(string):
    try:
        result = urlparse(string)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False