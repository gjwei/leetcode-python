#!/usr/env/python
# -*- coding: utf-8 -*-

__author__ = "gjwei"


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        left, right = head, head
        if m == 1:
            left = ListNode(0)
            left.next = head
        else:
            while m - 2:
                left = left.next
                m -= 1
        while n - 1:
            right = right.next
            n -= 1
        t = self.reverse(left, right.next)
        if m == 1:
            return t.next
        return head
        
        
        
        
        
    def reverse(self, head, end):
        p = q = head.next
        while p != end:
            t = p.next
            p.next = head.next
            head.next = p
            p = t
            q.next = p
        return head

l = ListNode(1)
l.next = ListNode(2)
s = Solution()
# t = s.reverse(l)
t = s.reverseBetween(l, 1, 1)
print t.val
