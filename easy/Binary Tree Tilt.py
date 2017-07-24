# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """  
        self.result = 0              
        self.sum_tree(root)
        return self.result
    def sum_tree(self, node):
        if not node:
            return 0
        left_sum = self.sum_tree(node.left)
        right_sum = self.sum_tree(node.right)
        self.result += abs(left_sum - right_sum)
        return node.val + left_sum + right_sum
            
            
        
s = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

print s.findTilt(root)
