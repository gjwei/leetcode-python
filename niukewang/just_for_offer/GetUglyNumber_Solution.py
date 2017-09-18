#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 9/13/17
  
"""
# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, n):
        # write code here
        dp = [1]
        index2, index3, index5 = 1, 1, 1
        f2, f3, f5 = 2, 3, 5
        while len(dp) < n:
            ugly = min(f2, f3, f5)
            dp.append(ugly)
            if ugly == f2:
                f2 = 2 * dp[index2]
                index2 += 1
            if ugly == f3:
                f3 = 3 * dp[index3]
                index3 += 1
            if ugly == f5:
                f5 = 5 * dp[index5]
                index5 += 1
        print(dp)
        return dp[n - 1]
    
    
                
        
s = Solution()
print(s.GetUglyNumber_Solution(11))

