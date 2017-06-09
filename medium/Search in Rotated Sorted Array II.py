#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 3/28/17
  
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        split_index = 0
        left, right = 0, len(nums) - 1
        


    