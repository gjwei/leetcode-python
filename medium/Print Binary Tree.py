#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 8/7/17
  
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        length = {}
        depth = {}
        m = self.get_depth(root, depth)
        n = self.get_length(root, length)
        result = [['' for _ in xrange(n)] for _ in xrange(m)]
        self._printTree(root, result, 0, 0, len(result[0]))
        return result
        
    def _printTree(self, root, result, row, col_left, col_right):
        if not root:
            return
        mid = (col_left + col_right) >> 1
        result[row][(col_left + col_right) // 2] = str(root.val)
        
        self._printTree(root.left, result, row + 1, col_left, mid)
        self._printTree(root.right, result, row + 1, mid + 1, col_right)
        
                
            
        
    def get_length(self, root, d):
        if not root:
            return 0
        if root in d:
            return d[root]
        left = self.get_length(root.left, d)
        right = self.get_length(root.right, d)
        result = 2 * max(left, right) + 1
        d[root] = result
        return result
        
    def get_depth(self, root, d):
        if not root:
            return 0
        if root in d:
            return d[root]
        left = self.get_depth(root.left, d)
        right = self.get_depth(root.right, d)
        result = max(left, right) + 1
        d[root] = result
        return result
    
a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.left.left = TreeNode(3)
a.left.left.left = TreeNode(5)
s = Solution()
t = s.printTree(a)
for i in t:
    print i
