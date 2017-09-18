#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 9/14/17
  
"""

class Solution:
    # s, pattern都是字符串
    def match(self, s, p):
        # write code here
        print("s: {s}, p: {p}".format(s=s, p=p))
        print(len(s), len(p))
        if len(s) == 0 and len(p) == 0:
            return True
        if len(s) != 0 and len(p) == 0:
            return False
        if len(p) > 1 and p[1] == '*':
            return (len(s) > 0 and self.match(s[1:], p[2:])) or self.match(s, p[2:]) or (len(s) > 0 and self.match(s[1:], p))
        if len(s) > 0 and (s[0] == p[0] or p[0] == '.'):
            return self.match(s[1:], p[1:])
        return False
        

s = Solution()
t = 'aa'
p = 'ab*a'
print(s.match(t, p))
                    
                
                
                