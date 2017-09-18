#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 8/13/17
  
"""
import sys


class Brick(object):
    
    def calculate(self, s):
        h = [0 for _ in xrange(256)]
        count = 0
        for c in s:
            if h[ord(c)] == 0:
                count += 1
            h[ord(c)] += 1
        
    
if __name__ == '__main__':
    s = sys.stdin.readline().strip()
    s = sys.stdin.readline().strip()
    b = Brick()
    print b.calculate(s)
