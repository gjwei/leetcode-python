#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 9/13/17
  
"""


# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
    
    # write code here
        if data[0] == k:
            left = -1
        else:
            left = self.upper_index(data, k - 1)
        return self.upper_index(data, k) - left
    
    def upper_index(self, data, k):
        left, right = 0, len(data) - 1
        while left < right:
            mid = (left + right) >> 1
            if data[mid] <= k < data[mid + 1]:
                return mid
            elif data[mid + 1] <= k:
                left = mid + 1
            else:
                right = mid
        return right
 
 
s = [3,3,3,3,4,5]

t = Solution()
print(t.GetNumberOfK(s, 3))
print(t.upper_index(s, 2))
print(t.upper_index(s, 3))