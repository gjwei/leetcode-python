# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.result = dict()
        self._findFrequentTreeSum(root)
        max_count, max_result = 0, []
        for key, value in self.result:
            if value > max_count:
                max_result = [key]
                max_count = value
            elif value == max_count:
                max_count.append(key)
        return max_result  

    def _findFrequentTreeSum(self, root):
        if not root:
            return 0
        if root.left:
            left_sum = self._findFrequentTreeSum(root.left)
        if root.right
        right_sum = self._findFrequentTreeSum(root.right)
        root_sum = left_sum + right_sum + root.val
        self.result[root_sum] = self.result.get(root_sum, 0) + 1
        return root_sum

