# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        stack = [root]
        p = TreeNode(0)
        while stack:
            q = stack.pop()
            p.right = q
            p = q
            if q.right:
                stack.append(q.right)
            if q.left:
                stack.append(q.left)
        return root

        
