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
        :rtype: List[List[int]]
        """

        result = []
        def _pathSum(node, current_sum, l):
            if not node:
                return
            current_sum += node.val
            l.append(node.val)
            if current_sum == sum:
                result.append(l[:])
                return
            _pathSum(node.left, current_sum, l[:])
            _pathSum(node.right, current_sum, l[:])
            return
        _pathSum(root, 0, [])
        return result
        