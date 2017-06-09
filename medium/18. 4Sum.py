#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 6/2/17
  
"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums, n = sorted(nums), len(nums)
        result = set()
        for i in xrange(n - 3):
            for j in xrange(i + 1, n - 2):
                if j > 1 and nums[j] == nums[j - 1] == nums[j - 2]:
                    continue
                new_target = target - nums[i] - nums[j]
                left, right = j + 1, n - 1
                while left < right:
                    current_tow_sum = nums[left] + nums[right]
                    if current_tow_sum == new_target:
                        temp_list = [nums[i], nums[j], nums[left], nums[right]]
                        result.add(tuple(temp_list))
                        right -= 1
                        left += 1
                    elif current_tow_sum > new_target:
                        right -= 1
                    else:
                        left += 1
        return list(list(t) for t in result)

s = Solution()
print s.fourSum([-3,-2,-1,0,0,1,2,3], 0)



    