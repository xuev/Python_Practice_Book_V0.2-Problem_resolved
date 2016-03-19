#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# Author:      xuev
# File:        Problem_9.py
# Version:     0.1
# License:     MIT Licence 
# Create Time: 2016/3/20 2:43
# Description: 
"""


def cumulative_product(list):
    p = 1
    m = 0
    list_product = []
    for n in list:
        p *= list[m]
        list_product.append(p)
        m += 1
    return list_product
