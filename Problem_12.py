#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# Author:      xuev
# File:        Problem_12.py
# Version:     0.1
# License:     MIT Licence 
# Create Time: 2016/3/20 3:35
# Description: 
"""


def group(list, size):
    list_group = []
    s = size
    m = 0
    while m + s < len(list):
        list_group.append(list[m:m + s])
        m += s
    list_group.append(list[m:])
    return list_group
