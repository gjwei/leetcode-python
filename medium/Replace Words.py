#!/usr/env/python
# -*- coding: utf-8 -*-


class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        s = sentence.split()
        dict = set(dict)
        result = []
        for w in s:
            result.append(self._root(w, dict))
        return ' '.join(result)
            
        
        
    def _root(self, word, dict):
        for i in xrange(len(word)):
            if word[:i] in dict:
                return word[:i]
        return word
    
s = Solution()
dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
print s.replaceWords(dict, sentence)