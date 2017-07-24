# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        ans = 0
        if root.left:
            if not root.left.left and not root.left.right:
                ans += root.left.val
            else:
                ans += self.sumOfLeftLeaves(root.left)
        if root.right:
            ans += self.sumOfLeftLeaves(root.right)
        return ans
        
        if not root:
            return 0
        stack = [root]
        result = 0
        while stack:
            p = stack.pop()
            if p.left and not p.left and not p.right:
                result += p.left.val
            if p.left:
                stack.append(p.left)
            if p.right:
                stack.append(p.right)
        return result
        
            
        
