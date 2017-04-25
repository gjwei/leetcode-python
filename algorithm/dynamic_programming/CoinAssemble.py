#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Created by gjwei on 3/13/17
  
"""
def coin_assemble(coins, target):
    d = [0] * (target + 1)
    for i in xrange(1, target+1):
        if i in coins:
            d[i] = 1
        else:
            d[i] = d[i - 1] + 1
            for coin in coins:
                if (i - coin >= 0):
                    d[i] = min(d[i - coin], d[i]) + 1
    return d[target]


coins = [1, 3, 5]
print coin_assemble(coins, 5)

    