#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 8/13/17
  
"""
def max_sum(arr):
    m, n = len(arr), len(arr[0])
    col_sum = [[0 for _ in range(n)] for _ in range(m)]
    for i in xrange(m):
        for j in xrange(n):
            if i == 0:
                col_sum[i][j] = arr[i][j]
            else:
                col_sum[i][j] = col_sum[i-1][j] + arr[i][j]
    result = 0
    for a in xrange(m):
        for c in xrange(a+1, m):
            ac_sum = [col_sum[c][j] - col_sum[a][j] for j in xrange(n)]
            result = max(result, _max_sum(ac_sum))
    return result

def _max_sum(nums):
    '''一维情况下求解数组的最大子数组和'''
    s, max_result = 0, 0
    for i in xrange(len(nums)):
        if s >= 0:
            s += nums[i]
            max_result = max(max_result, s)
        else:
            s = 0
    return max_result

if __name__ == '__main__':
    a = [3, -2, 1, -8, 3, -1]
    print _max_sum(a)
            

