#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author: xuev
@File: Problem_5.py
@Version: 
@License: MIT Licence 
@Create Time: 2016/3/17 22:30
@Description: 
"""


# Problem 5: Write a function factorial to compute factorial of a number.
# Can you use the product function defined in the previous example to compute factorial?

def factorial(x):
    s = 1
    n = 1
    while n <= x:
        s *= n
        n += 1
    return s
