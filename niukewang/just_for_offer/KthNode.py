#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 9/15/17
  
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        d = {}
        _ = self.count(pRoot, d)
        return self._kth_node(pRoot, k, d)
        
    def _kth_node(self, root, k, d):
        left_count = self.count(root.left, d)
        if left_count == k - 1:
            return root
        elif left_count < k - 1:
            return self._kth_node(root.right, k - left_count - 1, d)
        else:
            return self._kth_node(root.left, k, d)
         
    def count(self, root, d):
        if root is None:
            return 0
        if root in d:
            return d[root]
        count = 1
        result = count + self.count(root.left, d) + self.count(root.right, d)
        d[root] = result
        return result