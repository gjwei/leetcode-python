#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 8/27/17
  
"""

import sys

def longest(x, f, d, p):
    """
    :param x: rent
    :param f: fruits have
    :param d: money have
    :param p: one apple p money
    :return:
    """
    # 钱不足
    if d // x <= f:
        return d // x
    # 苹果不足
    day_money = p + x
    total_money = f * p + d
    return total_money // day_money

if __name__ == '__main__':
    x, f, d, p = map(int, sys.stdin.readline().strip().split())
    print longest(x, f, d, p)