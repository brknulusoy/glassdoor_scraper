# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 12:49:46 2022

@author: frost
"""

#import text_split_scrapper as tss
import glassdoor_scraper as gs

df = gs.glassdoor_scraper("email", "password", "job", "city")