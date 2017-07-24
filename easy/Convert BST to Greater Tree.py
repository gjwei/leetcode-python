# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        left_sum = self.calculate_sum(root.left)

    
    def calculate_sum(self, root, sum):
        if not root:
            return sum
        right = self.calculate_sum(root.right, sum)
        left = self.calculate_sum(root.left, right + root.val)
        root.val += right
        return left
        
        
        