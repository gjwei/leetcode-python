#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 3/15/17
  
"""


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        result = []

        for k in xrange(min(4, num) + 1):
            up_list = [0] * 4
            down_list = [0] * 6
            up_result = []
            down_result = []
            self.dfs(up_list, 0, k, up_result)
            self.dfs(down_list, 0, num - k, down_result)

            for i in range(len(up_result)):
                for j in range(len(down_result)):
                    s = self.get_time_string(up_result[i], down_result[j])
                    if s:
                        result.append(s)
        return result


    def dfs(self, array, index, k, result):
        if k == 0:
            result.append(array[:])
            return
        if index == len(array):
            return
        for i in xrange(index, len(array)):
            if array[i] == 0:
                array[i] = 1
                self.dfs(array, i + 1, k - 1, result)
                array[i] = 0


    def get_time_string(self, up_list, down_list):
        hours, minutes = 0, 0
        for i in xrange(len(up_list)):
            hours += up_list[i] << i
        for j in xrange(len(down_list)):
            minutes += down_list[j] << j
        if hours > 11 or minutes > 59:
            return None
        return "%d:%02d" % (hours, minutes)





s = Solution()
print s.readBinaryWatch(2)