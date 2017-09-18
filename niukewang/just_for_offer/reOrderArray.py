#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 9/10/17
  
"""
class Solution:
    def reOrderArray(self, array):
        return [n for n in array if n & 1] + [n for n in array if n & 1 == 0]
        

        

