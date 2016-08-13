#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author: xuev
@File: Problem_002.py
@Version: 
@License: MIT Licence 
@Create Time: 2016/3/17 22:11
@Description: 
"""


# Problem 2: Python has a built-in function sum to find sum of all elements of a list.
# Provide an implementation for sum.

def sum(list):
    s = 0
    for x in list:
        s += x
    return s
