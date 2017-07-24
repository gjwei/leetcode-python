# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.result = 0
        _ = self._tree_count(root, k)
        return self.result

    def _tree_count(self, root, k):
        if not root:
            return 0
        left = self._tree_count(root.left, k)
        if left + 1 == k:
            self.result = root.val
        right = self._tree_count(root.right, k - left - 1)
        return left + right + 1

        
        
        