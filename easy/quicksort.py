#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Created by gjwei on 2017/2/20
 
"""
def qsort(list):
    if not list:
        return[]
    else:
        pivot = list[0]
        left = [x for x in list if x < pivot]
        right = [x for x in list[1:] if x >= pivot]
        return qsort(left) + [pivot] + qsort(right)

qs = lambda xs : ( (len(xs) <= 1 and [xs]) or [qs([x for x in xs[1:] if x < xs[0]] ) + [xs[0]] + qs( [x for x in xs[1:] if x >= xs[0]])])[0]
