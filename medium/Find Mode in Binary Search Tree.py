# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack= [root]
        if not root:
            return []
        d = {}
        while stack:
            p = stack.pop()
            d[p.val] = d.get(p.val, 0) + 1
            if p.right:
                stack.append(p.right)
            if p.left:
                stack.append(p.left)
        print d   
        result, max_count = [], 0
        for key, val in d.iteritems():
            if val > max_count:
                result = [key]
                max_count = val
            elif val == max_count:
                result.append(key)
        return result

t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(2)

s = Solution()
print s.findMode(t)
        