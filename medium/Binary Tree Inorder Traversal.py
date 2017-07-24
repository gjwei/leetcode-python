#coding: utf-8
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack, p = [], root
        result = []
        while stack or p:
            while p:
                stack.append(p)
                p = p.left
            q = stack.pop()
            result.append(q.val)
            p = q.right
        return result
s = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

print s.inorderTraversal(root)

        