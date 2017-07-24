# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        

    def max_depth(self, root):
        
    
    # def diameterOfBinaryTree(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     self.result = 0
    #     self._diameterOfBinaryTree(root)
    #     return self.result

    
    # def _diameterOfBinaryTree(self, root):
    #     if not root:
    #         return
    #     self.result = max(self.calculate_max_height(root.left) + self.calculate_max_height(root.right), self.result)
    #     return


    # def calculate_max_height(self, root):
    #     if not root:
    #         return 0
    #     return max(self.calculate_max_height(root.left), self.calculate_max_height(root.right)) + 1