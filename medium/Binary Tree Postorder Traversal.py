# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        pre, p = None, root
        if not root: return []
        stack, result = [], []
        while stack or p:
            if p:
                stack.append(p)
                p = p.left
            else:
                if pre == stack[-1].right:
                    cur = stack.pop()
                    result.append(cur.val)
                    pre = cur
                else:
                    p = stack[-1].right
                    pre = None
        return result

t = TreeNode(0)
t.left = TreeNode(1)
t.right = TreeNode(2)
t.left.left = TreeNode(3)
s = Solution()
print s.postorderTraversal(t)



            
            
        