#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 8/4/17
  
"""


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        h = [0 for i in xrange(26)]
        for t in tasks:
            h[ord(t) - ord('A')] += 1
        h = sorted(h)
        print h
        index = 25
        while index >= 0 and h[index] == h[-1]:
            index -= 1
        print index
        return max(len(tasks), (h[25] - 1) * (n + 1) + (25 - index))


s = Solution()
task = ['A','A','A','B','B','B']
n = 2
print s.leastInterval(task, n)