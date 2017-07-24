# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        return self._sortedListToBST(head, None)
    
    def _sortedListToBST(self, head, end):
        if not head:
            return None
        mid_node = self.find_mid_listnode_position(head, end)
        root = TreeNode(mid_node.val)
        root.left = self._sortedListToBST(head, mid)
        root.right = self._sortedListToBST(mid.next, end)
        return root


    def find_mid_listnode_position(self, head, end):
        left, right = head, head
        while right != end and right.next != end and right.next.next != end:
            left = left.next
            right = right.next.next
        return left
        