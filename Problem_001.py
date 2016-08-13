#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author: xuev
@File: Problem_001.py
@Version: 
@License: MIT Licence 
@Create Time: 2016/3/17 22:13
@Description: 
"""

# Problem 1: What will be the output of the following program?
x = [0, 1, [2]]
x[2][0] = 3
print x
x[2].append(4)
print x
x[2] = 2
print x

# Answer:
# [0, 1, [3]]
# [0, 1, [3, 4]]
# [0, 1, 2]
