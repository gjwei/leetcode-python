#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 9/11/17
  
"""


def multiply( A):
    # write code here
    b = [1 for _ in xrange(len(A))]
    # left to right
    for i in xrange(1, len(A)):
        b[i] = b[i - 1] * A[i - 1]
    print b
    for i in xrange(len(A) - 2, -1, -1):
        b[i] = b[i] * A[i + 1]
    return b

if __name__ == '__main__':
    a = [1, 3, 4, 5]
    print multiply(a)