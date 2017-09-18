#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 9/11/17
  
"""

class Solution:
    def VerifySquenceOfBST(self, sequence):
        
        if len(sequence) == 0:
            return False
        return self._verify(sequence)
    
    def _verify(self, sequence):
        if len(sequence) == 0:
            return True
        root_val = sequence[-1]
        seperate_index = len(sequence) - 1
        while seperate_index >= 1 and sequence[seperate_index - 1] >= root_val:
            seperate_index -= 1
        left = sequence[:seperate_index]
        for n in left:
            if n >= root_val:
                return False
        return self._verify(left) and self._verify(sequence[seperate_index:-1])
    
s = Solution()
a = [4,8,6,12,16,14,10]

print(s.VerifySquenceOfBST(a))
        