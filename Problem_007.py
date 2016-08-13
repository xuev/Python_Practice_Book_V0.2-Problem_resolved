#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author: xuev
@File: Problem_007.py
@Version: 
@License: MIT Licence 
@Create Time: 2016/3/17 22:42
@Description: 
"""


def min(lt):
    l = len(lt)
    n = 0
    x = lt[n]
    if type(x) == int:
        y = x
    elif type(x) == str:
        y = len(x)
    else:
        return "Error: Type of the list element must be int or str."
    if l == 0:
        return "Error: Empty list given."
    if l == 1:
        return x
    while n < l - 1:
        m = n + 1
        if type(lt[m]) == int:
            z = lt[m]
        elif type(lt[m]) == str:
            z = len(lt[m])
        else:
            return "Error: Type of the list element must be int or str."
        if y <= z:
            n += 1
        else:
            x = lt[m]
            if type(x) == int:
                y = x
            else:
                y = len(x)
            n += 1
    return x


def max(lt):
    l = len(lt)
    n = 0
    x = lt[n]
    if type(x) == int:
        y = x
    elif type(x) == str:
        y = len(x)
    else:
        return "Error: Type of the list element must be int or str."
    if l == 0:
        return "Error: Empty list given."
    if l == 1:
        return x
    while n < l - 1:
        m = n + 1
        if type(lt[m]) == int:
            z = lt[m]
        elif type(lt[m]) == str:
            z = len(lt[m])
        else:
            return "Error: Type of the list element must be int or str."
        if y >= z:
            n += 1
        else:
            x = lt[m]
            if type(x) == int:
                y = x
            else:
                y = len(x)
            n += 1
    return x
