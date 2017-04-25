#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Created by gjwei on 3/13/17
  
"""
def lis(nums):
    dp = [1] * len(nums)
    n = len(nums)
    if n == 0:
        return 0
    for i in xrange(1, n):
        for j in xrange(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def lis_dp(nums):
    n = len(nums)

    dp = [nums[0]]

    for i in xrange(1, n):
        insert_place = find_replace_position(dp, 0, len(dp) - 1, nums[i])
        if insert_place == len(dp):
            dp.append(nums[i])
        elif insert_place >= 0 and insert_place < len(dp):
            dp[insert_place] = nums[i]
    return len(dp)



def find_replace_position(a, left, right, target):
    if len(a) == 0:
        return 0
    if left > right:
        return -1
    if a[left] >= target:
        return left
    if a[right] < target:
        return right + 1
    while left < right:
        mid = (left + right) // 2
        if a[mid] > target:
            right = mid - 1
        elif a[mid] < target and a[mid + 1] > target:
            return mid + 1
        else:
            left = mid + 1
    return -1



a = [2, 1, 3, 6, 4, 8, 9, 7]
print lis_dp(a)



    