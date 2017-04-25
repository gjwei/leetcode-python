#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 3/29/17
  
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or (not head.next):
            return head
        even = p1 = head

        odd = p2 = head.next
        p = head.next.next
        p1.next = None
        p2.next = None

        while p:
            p1.next = p
            p1 = p1.next
            p = p.next
            if p:
                p2.next = p
                p2 = p2.next
                p = p.next
        p1.next = odd
        return even

s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

h = s.oddEvenList(head)
print h.val, h.next.val