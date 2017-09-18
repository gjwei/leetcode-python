#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 9/11/17
  
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root is None:
            return []
        result = []
        queue = [root]
        while queue:
            length = len(queue)
            for i in xrange(length):
                p = queue.pop(0)
                result.append(p.val)
                if p.left:
                    queue.append(p.left)
                if p.right:
                    queue.append(p.right)
        return result
