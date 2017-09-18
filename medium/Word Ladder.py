#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 7/24/17
  
"""


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        result = 0
        pre_distance = self.calculate(beginWord, endWord)
        while beginWord != endWord:
            result += 1
            if self.calculate(beginWord, endWord) == 1:
                break
            transform = False
            for w in wordList:
                if self.calculate(beginWord, w) == 1 and self.calculate(endWord, w) <= pre_distance:
                    beginWord = w
                    transform = True
                    pre_distance = self.calculate(endWord, w)
                    break
                    break
            if not transform:
                return 0
        return result
        
    def calculate(self, w1, w2):
        result = 0
        for i in xrange(len(w1)):
            if w1[i] != w2[i]:
                result += 1
        return result
    
    
b = 'hit'
e = 'cog'
w = ["hot","dot","dog","lot","log","cog"]
s = Solution()
print s.ladderLength(b, e, w)