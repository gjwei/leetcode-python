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
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        result = []
        self._dfs(root, expectNumber, result, [])
        return result
    
    def _dfs(self, root, expect, result, path):
        if root is None:
            return
        if root.left is None and root.right is None:
            if expect - root.val == 0:
                path.append(root.val)
                result.append(path)
            return
        self._dfs(root.left, expect - root.val, result, path + [root.val])
        self._dfs(root.right, expect - root.val, result, path + [root.val])
        
 
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(12)
root.left.left = TreeNode(4)
root.left.right = TreeNode(7)

s = Solution()
print s.FindPath(root, 22)