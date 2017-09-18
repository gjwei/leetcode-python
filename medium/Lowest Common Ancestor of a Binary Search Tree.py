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
        _ = self._lca(root, p, q, d)
        queue = [root]
        while queue:
            p = queue.pop(0)
            left = d[p] or d[p.left]
            right = d[p.right]
            if left and right:
                return p
            elif left and p.left:
                queue.append(p.left)
            elif right and p.right:
                queue.append(p.right)
        return None
        
    
    def _lca(self, root, p, q, d):
        if not root:
            return False
        if root in d:
            return d[root]
        if root == p or root == q:
            d[root] = True
            return True
        result = self._lca(root.left, p, q, d) or self._lca(root.right, p, q, d)
        d[root] = result
        return result
        
    
    