#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 4/25/17
  
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        #p = n
        for i in xrange(n):
            n = self.generate_count_and_say(n)
        return n


    def generate_count_and_say(self, num):
        s = str(num)
        count, result, i = 1, [], 0
        for i in xrange(0, len(s)):
            if i == 0:
                continue
            if s[i] == s[i - 1]:
                count += 1
            else:
                result.append(str(count) + s[i - 1])
                count = 1

        result.append(str(count) + s[i])
        return ''.join(result)

s = Solution()
print s.countAndSay(44)