#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 8/13/17
  
"""


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if len(arr) <= k:
            return arr
        index = self._bs(arr, x)
        print index
        result = [arr[index]]
        left, right = index - 1, index + 1
        while len(result) < k and (left >= 0 or right < len(arr)):
            if left >= 0 and right < len(arr):
                if x - arr[left] <= arr[right] - x:
                    result.insert(0, arr[left])
                    left -= 1
                else:
                    result.append(arr[right])
                    right += 1
            elif left >= 0:
                result.insert(0, arr[left])
                left -= 1
            else:
                result.append(arr[right])
                right += 1
        return result
        
        
        
    def _bs(self, arr, x):
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) >> 1
            if arr[mid] == x:
                return mid
            elif arr[mid] < x < arr[mid + 1]:
                return mid
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid
        return right

s = Solution()
print s.findClosestElements([1,2,3,4,5], 4, -1)