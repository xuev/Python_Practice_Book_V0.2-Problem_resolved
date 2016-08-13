#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author: xuev
@File: Problem_006.py
@Version: 
@License: MIT Licence 
@Create Time: 2016/3/17 22:36
@Description: 
"""


# Problem 6: Write a function reverse to reverse a list.
# Can you do this without using list slicing?

def reverse(lt):
    x = len(lt)
    tl = []
    while x > 0:
        tl.append(lt[x - 1])
        x -= 1
    return tl
