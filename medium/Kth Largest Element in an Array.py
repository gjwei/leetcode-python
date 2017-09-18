#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 8/17/17
  
"""


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k = len(nums) - k
        left, right = 0, len(nums) - 1
        while left <= right:
            index, value = self._partition(nums, left, right)
            if index == k:
                return value
            elif index < k:
                left = index + 1
            else:
                right = index - 1
        raise ValueError
        
    def _partition(self, nums, left, right):
        p = nums[right]
        index = left
        for i in xrange(left, right):
            if nums[i] < p:
                nums[i], nums[index] = nums[index], nums[i]
                index += 1
        nums[index], nums[right] = nums[right], nums[index]
        return index, nums[index]
    

if __name__ == '__main__':
    s = Solution()
    nums = [3,2,1,5,6,4]
    print s.findKthLargest(nums, 2)
    
        
            
        
        