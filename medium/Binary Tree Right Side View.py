#coding: utf-8
#层序遍历取左右边的就可以啦

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack1, stack2 = [root], []
        result = []
        while stack1:
            result.append(stack1[-1].val)
            while stack1:
                p = stack1.pop(0)
                if p.left:
                    stack2.append(p.left)
                if p.right:
                    stack2.append(p.right)
            stack1, stack2 = stack2, stack1
        return result
                


        