#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 7/24/17
  
"""


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count, result, start = 0, 0, 0
        hash_list = [0 for _ in xrange(26)]
        for end in xrange(len(s)):
            hash_list[ord(s[end]) - ord('A')] += 1
            count = max(count, hash_list[ord(s[end]) - ord('A')])
            while end - start + 1 - count > k:
                hash_list[ord(s[start]) - ord('A')] -= 1
                start += 1
            result = max(result, end - start + 1)
        return result

s = Solution()
t = "ABAB"
k = 2
print s.characterReplacement(t, k)

            
            

