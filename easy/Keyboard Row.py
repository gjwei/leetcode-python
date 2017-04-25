#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 3/29/17
  
"""


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        alphabet1 = set(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'])
        alphabet2 = set(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'])
        alphabet3 = set(['z', 'x', 'c', 'v', 'b', 'n', 'm'])
        alphabets = [alphabet1, alphabet2, alphabet3]
        for word in words:
            if self.is_keyboard_row(word, alphabets):
                result.append(word)
        return result


    def is_keyboard_row(self, word, alphabets):
        for alphabet in alphabets:
            flag = True
            for i in word.lower():
                if i not in alphabet:
                    flag = False
            if flag:
                return flag
        return False

s = Solution()
w = ["Hello", "Alaska", "Dad", "Peace"]
print s.findWords(w)