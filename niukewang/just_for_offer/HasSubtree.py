#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 9/10/17
  
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if pRoot2 is None or pRoot1 is None:
            return False
        result = self.isSubTree(pRoot1, pRoot2)
        if result:
            return result
        result |= (self.isSubTree(pRoot1.left, pRoot2))
        return result if result else result or self.isSubTree(pRoot1.right, pRoot2)
        
        
        
    def isSubTree(self, root1, root2):
        if root2 is None:
            return True
        if root1 is None or root1.val != root2.val:
            return False
        return self.isSubTree(root1.left, root2.left) and self.isSubTree(root1.right, root2.right)
        # if root1 is None and root2 is None:
        #     return True
        # elif (root1 is None and root2 is not None) or \
        #         (root1 is not None and root2 is None) \
        #          or (root1.val != root2.val):
        #     return False
        # return self.isSubTree(root1.left, root2.left) and self.isSubTree(root1.right, root2.right)
        #
        #
