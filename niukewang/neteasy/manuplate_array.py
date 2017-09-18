#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 8/27/17
  
"""
import sys

def manuplate(nums):
    even = [nums[i] for i in xrange(len(nums)) if i & 1 == 1]
    odd = [nums[i] for i in xrange(len(nums)) if i & 1 == 0]
    if len(nums) & 1 == 1:
        return odd[::-1] + even
    else:
        return even[::-1] + odd
    

if __name__ == '__main__':
    _ = sys.stdin.readline()
    nums = sys.stdin.readline().strip().split()
    result = manuplate(nums)
    
    print ' '.join(result)
    

