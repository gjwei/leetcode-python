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
        prefix_sum = {0: 1}
        return self._pathSum(root, 0, sum, prefix_sum)
        
    def _pathSum(self, root, cur_sum, target, prefix_sum):
        if not root:
            return 0
        cur_sum += root.val
        result = prefix_sum.get(cur_sum - target, 0)
        prefix_sum[cur_sum] = prefix_sum.get(cur_sum, 0) + 1
        result += self._pathSum(root.left, cur_sum, target, prefix_sum) + \
                  self._pathSum(root.right, cur_sum, target, prefix_sum)
        prefix_sum[cur_sum] -= 1
        return result