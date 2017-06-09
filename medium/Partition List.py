# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        new_head = ListNOde(x - 1)
        p = new_head
        while p and p.next:
            if p.next.val < x:
                p = p.next
            else:
                p.next = p.next.next
        