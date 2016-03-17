#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author: xuev
@File: Problem_4.py
@Version: 
@License: MIT Licence 
@Create Time: 2016/3/17 22:24
@Description: 
"""


# Problem 4: Implement a function product,
# to compute product of a list of numbers.

def product(list):
    s = 1
    for x in list:
        s *= x
    return s
