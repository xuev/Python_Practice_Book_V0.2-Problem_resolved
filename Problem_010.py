#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# Author:      xuev
# File:        Problem_010.py
# Version:     0.1
# License:     MIT Licence 
# Create Time: 2016/3/20 2:48
# Description: 
"""


def unique(list):
    list_unique = []
    m = 0
    for n in list:
        if list[m] not in list_unique:
            list_unique.append(list[m])
            m += 1
        else:
            m += 1
    return list_unique
