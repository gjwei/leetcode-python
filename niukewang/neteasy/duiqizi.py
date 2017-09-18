#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 8/27/17
  
"""
import sys

def min_step(x, y):
    distances = [[0 for _ in range(50)] for _ in range(50)]
    result = [50 for _ in xrange(len(x))]
    for i in xrange(len(x)):
        for j in xrange(i + 1, len(x)):
            distances[i][j] = distances[j][i] = distance(x, y, i, j)
        dis = sorted(distances[i][:len(x)])
        print dis
        for index in xrange(len(x)):
            result[index] = min(result[index], sum(dis[:index+1]))
    return result
        
def distance(x, y, i, j):
    return abs(x[i] - x[j]) + abs(y[i] - y[j])

if __name__ == '__main__':
    _ = sys.stdin.readline()
    x = map(int, sys.stdin.readline().split())
    y = map(int, sys.stdin.readline().split())
    
    print ' '.join(str(i) for i in min_step(x, y))
    
