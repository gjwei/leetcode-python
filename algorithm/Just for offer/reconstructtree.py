#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 4/27/17
  
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        ###
        if not len(pre):
            return None
        root = TreeNode(pre[0])
        index = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:index + 1], tin[:index])
        root.right = self.reConstructBinaryTree(pre[index+1:], tin[index+1])
        return root




    