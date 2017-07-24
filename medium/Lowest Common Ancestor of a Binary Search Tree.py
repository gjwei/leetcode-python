# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        d = {}
    
    def _lca(self, root, p, q, d):
        
    
    def find_node(root, p, q):
        if not root:
            return False
        if root.val == p or root.val == q:
            return True
        left = self.find_node(root.left, p, q)
        right = self.find_node(root.right, p, q)
        return left and right
        # if not root:
        #     return False
        # if root in d:
        #     return d[root]
        # if root.val == p or root.val == q:
        #     d[root] = True
        #     return True
        # left = self._lca(root.left, p, q, d)
        # right = self._lca(root.right, p, q, d)
        # result = left and right
        # d[root] = result
        # return result