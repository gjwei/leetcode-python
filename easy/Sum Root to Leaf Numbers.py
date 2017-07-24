# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        self._sumNumbers(root, '')
        return 

    def _sumNumbers(self, root, s):
        if not root:
            self.result = self.result + int(s) if len(s) > 0 else self.result
            return
        self._sumNumbers(root.left, s+str(root.val))
        self._sumNumbers(root.right, s+str(root.val))
        return
        