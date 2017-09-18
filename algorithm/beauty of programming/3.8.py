#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 8/17/17
  
"""
"""求二叉树节点中的最大距离"""


class TreeNode(object):
    def __init__(self, val):
        self.val  = val
        self.left, self.right = None, None
        
def max_distance(root):
    if not root:
        return 0
    return max(max_distance(root.left), max_distance(root.right), get_distance(root.left)+get_distance(root.right))

    

def get_distance(root):
    if not root:
        return 0
    left = get_distance(root.left)
    right = get_distance(root.right)
    return max(left, right) + 1
    
