#!/usr/env/python
# -*- coding: utf-8 -*-
# __author__ = ‘gjwei‘

class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        if len(pairs) == 0:
            return 0
        pairs = sorted(pairs, key=lambda x: x[1])
        result = 1
        last_pos = pairs[0][1]
        for i in xrange(1, len(pairs)):
            if pairs[i][0] > last_pos:
                result += 1
                last_pos = pairs[i][1]
            else:
                continue
        return result
s = Solution()
a = [[1,2], [1, 3], [3, 4], [5, 7]]
print s.findLongestChain(a)
            
            
            
        