#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 9/11/17
  
"""


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        
        return 1 + min(self.minDistance(word1, word2[1:]),
                       self.minDistance(word1[1:], word2),
                       self.minDistance(word1[1:], word2[1:]))
    
    def _min_distance(self, w1, index1, w2, index2, d):
        if index1 == len(w1):
            return len(w2[index2:])
        
        if index2 == len(w2):
            return len(w1[index1:])
        
        if (index1, index2) in d:
            return d[(index1, index2)]
        
        if w1[0] == w2[0]:
            result = self._min_distance(w1, index1 + 1, w2, index2 + 1, d)
        else:
            result = 1 + min(
                self._min_distance(w1, index1, w2, index2 + 1, d),
                self._min_distance(w1, index1 + 1, w2, index2, d),
                self._min_distance(w1, index1 + 1, w2, index2 + 1, d)
            )
            
        d[(index1, index2)] = result
        
        return result
s = Solution()
w1 = 'hello'
w2 = 'hahall'
print s.minDistance(w1, w2)
d = {}
print s._min_distance(w1, 0, w2, 0, d)
print d