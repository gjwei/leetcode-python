#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 7/26/17
  
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root in (None, p, q):
            return root
        left, right = self.lowestCommonAncestor(root.left, p, q), \
                      self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left or right
        
        
    #
    #     d = {}
    #     queue = [root]
    #     while queue:
    #         t = queue.pop(0)
    #         cur_node = t == q or t == p
    #         left, right = self._lca(t.left, p, q, d) or self._lca(t.left, p, q, d), self._lca(t.right, p, q, d)
    #         if (left and right) or (cur_node and left) or (cur_node and right):
    #             return t
    #         if left and t.left:
    #             queue.append(t.left)
    #         elif right and t.right:
    #             queue.append(t.right)
    #     return None
    #
    #
    # def _lca(self, root, p, q, d):
    #     if not root:
    #         return False
    #     if root in d:
    #         return d[root]
    #     if root == p or root == q:
    #         d[root]  = True
    #         return True
    #     result = self._lca(root.left, p, q, d) or self._lca(root.right, p, q, d)
    #     d[root] =result
    #     return result
