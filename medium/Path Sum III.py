# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.result = 0
        self._pathSum(root, sum, 0)
        return self.result

    def _pathSum(self, root, sum, cur_sum):
        if cur_sum == sum:
            self.result += 1
            return
        if not root or cur_sum > sum:
            return
        cur_sum += root.val
¬        self._pathSum(root.right, sum, cur_sum)
        cur_sum -= root.val
        self._pathSum(root.left, sun, cur_sum)
        self._pathSum(root.right, sum, cur_sum)
        return

