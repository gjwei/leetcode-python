#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 9/14/17
  
"""
class Solution:
    # 返回对应char
    s = []
    h = [0 for _ in range(128)]
    def FirstAppearingOnce(self):
        # write code here
        for c in self.s:
            if self.h[ord(c)] == 1:
                return c
        return '#'
        
    def Insert(self, char):
        # write code here
        self.s.append(char)
        self.h[ord(char)] += 1
        
if __name__ == '__main__':
    s = Solution()
    while 1:
        char = input()
        s.Insert(char)
        print(s.FirstAppearingOnce())
        