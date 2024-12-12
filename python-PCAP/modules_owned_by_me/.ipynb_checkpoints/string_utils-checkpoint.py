#!/usr/bin/env python3
""" string_utils.py is a sample Python module that devides string to two """

import math
def halve_string(input_string):
    length = math.ceil(len(input_string) / 2)
    first_half = input_string[0:length]
    second_half = input_string[length:]
    result = (first_half, second_half)
    return result



# # ceil(), floor(), trunc()
# print(math.ceil(3.6) ) # ceil rounds the num to the nearest integer (never less the num itself)
# print(math.floor(3.6 ) # floor rounds the num to the nearest integer "not greater" then num
# print(math.trunc(3.6 ) # just removes the decimals 