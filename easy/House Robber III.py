# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
# if not root:
#             return 0
#         val = 0
#         if root.left:
#             val += self.rob(root.left) + self.rob(root.right)
#         if root.right:
#             val += self.rob(root.right.left) + self.rob(root.right.right)
#         return max(val + root.val, self.rob(root.left) + self.rob(root.right))
         d = {}
         return self._rob(root, d)
        
    def _rob(self, root, d):
        if not root: return 0
        if root in d: return d[root]
        val = 0
        if root.left:
            val += self._rob(root.left.left, d) + self._rob(root.left.right, d)
        if root.right:
            val += self._rob(root.right.left, d) + self._rob(root.right.left, d)
        result = max(val + root.val, self._rob(root.left) + self._rob(root.right))
        d[root] = result
        return result
        
