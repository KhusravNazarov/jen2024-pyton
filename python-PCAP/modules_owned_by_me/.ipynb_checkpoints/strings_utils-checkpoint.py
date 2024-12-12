#!/usr/bin/env python3
""" strings_utils.py is a sample Python module that devides list of strings to two """

import math
from string_utils import halve_string as hs
def halve_strings(string_list):
    
    list_of_string = [hs(s) for s in string_list]
    return list_of_string




# # ceil(), floor(), trunc()
# print(math.ceil(3.6) ) # ceil rounds the num to the nearest integer (never less the num itself)
# print(math.floor(3.6 ) # floor rounds the num to the nearest integer "not greater" then num
# print(math.trunc(3.6 ) # just removes the decimals 