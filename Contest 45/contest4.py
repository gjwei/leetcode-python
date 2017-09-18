#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 8/13/17
  
"""


class Solution(object):
    def newInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.count(n)
    
    def count(self, n):
        count_9 = [0 for _ in xrange(10)]
        for i in xrange(1, 10):
            count_9[i] = count_9[i - 1] * 9 + 10 ** (i - 1)
        print count_9
        result = 0
        while n >= 10:
            for i in range(9, 0, -1):
                t = n // (10 ** i)
                if t > 0:
                    result += t * count_9[i - 1]
                    n %= (10 ** i)
                    break
        return result
            
                
s = Solution()
print s.newInteger(59)
