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
        self.result = None
        _ = self.travel(root, p, q)
        return self.result

    def travel(self, root, p, q):
        if not root:
            return False
        if root == p or root == q:
            return True
        left = self.travel(root.left, p, q)
        right = self.travel(root.right, p, q)
        if left and right:
            self.result = root
        return left or right