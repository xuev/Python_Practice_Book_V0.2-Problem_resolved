#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# Author:      xuev
# File:        Problem_8.py
# Version:     0.1
# License:     MIT Licence 
# Create Time: 2016/3/20 2:36
# Description: 
"""


def cumulative_sum(list):
    s = 0
    m = 0
    list_sum = []
    for n in list:
        s += list[m]
        list_sum.append(s)
        m += 1
    return list_sum
