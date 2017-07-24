# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if d == 1:
            left, right = root.left, root.right
            root.left = TreeNode(v)
            root.right = TreeNode(v)
            root.left.left = left
            root.right.right = right
            return root
        root.left = self.addOneRow(root.left, v, d - 1)
        root.right = self.addOneRow(root.right, v, d - 1)
        return root
        