#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 9/14/17
  
"""

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, root):
        slow, fast = root, root
        
        