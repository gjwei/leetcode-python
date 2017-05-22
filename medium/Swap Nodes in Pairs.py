#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 4/26/17
  
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        n = head.next
        head.next = self.swapPairs(n.next)
        n.next = head
        return n

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)

s = Solution()
b = s.swapPairs(a)
while b:
    print b.val
    b = b.next


    