#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# Author:      xuev
# File:        Problem_011.py
# Version:     0.1
# License:     MIT Licence 
# Create Time: 2016/3/20 2:53
# Description: 
"""


def dups(list):
    list_dups = []
    m = 0
    for n in list:
        if list[m] in list[m+1:] and list[m] not in list_dups:
            list_dups.append(list[m])
            m += 1
        else:
            m += 1
    return list_dups
