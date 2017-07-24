# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        elif not root.left and not root.right:
            return str(root.val)
        elif not root.left:
            return str(root.val) + '()' + + '(' + str(self.tree2str(root.right)) + ')'
        elif not root.right:
            return str(root.val) + '(' + self.tree2str(root.left) + ')'
        else:
            return root.val + '(' + self.tree2str(root.left) + ')' + '(' + self.tree2str(root.right) + ')'
