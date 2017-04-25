#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 3/25/17
  
"""


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        pre_sum = []
        cur_sum = []
        for i in range(n):
            if i == 0:
                cur_sum = triangle[i][:]
            else:
                pre_sum = cur_sum[:]
                cur_sum = []
                for j in range(len(triangle[i])):
                    if j == 0:
                        cur_sum.append(pre_sum[0] + triangle[i][0])
                    elif j == len(pre_sum):
                        cur_sum.append(pre_sum[j - 1] + triangle[i][j])
                    else:
                        cur_sum.append(min(pre_sum[j - 1], pre_sum[j]) + triangle[i][j])
                #help_list.append(cur_sum)
        return min(cur_sum)


s = Solution()
a = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print s.minimumTotal(a)



    