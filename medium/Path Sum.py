# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        def get_sum(node, current_sum):
            if not node or current_sum > sum:
                return False
            if current_sum == sum and node and node.left and node.right:
                return True
            return get_sum(node.left, current_sum+node.val) or get_sum(node.right, current_sum+node.val)
        return get_sum(root, 0)