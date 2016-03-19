#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# Author:      xuev
# File:        Problem_13.py
# Version:     0.1
# License:     MIT Licence 
# Create Time: 2016/3/20 4:21
# Description: 
"""

# Un resolved...

def lensort(list):
    y = len(list)
    if y > 0:
        lensort_iter(list)
        y -= 1
    else:
        return lensort_iter(list)


def lensort_iter(list):
    m = 1
    while m < len(list):
        if len(list[m]) < len(list[m - 1]):
            x = list[m]
            list.pop(m)
            list.insert(m - 1, x)
        m += 1
    return list
