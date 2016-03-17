#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author: xuev
@File: Problem_3.py
@Version: 
@License: MIT Licence 
@Create Time: 2016/3/17 22:16
@Description: 
"""

# Problem 3: What happens when the above sum function is called with a list of strings?
# Can you make your sum function work for a list of strings as well.
def sum(list):
    s = ""
    for x in list:
        s += x
    return s
