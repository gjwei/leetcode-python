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
        pre_m_node, n_node = head, head
        while m:
            pre_m_node = pre_m_node.next
            m -= 1
        while n:
            n_node = n_node.next
            n -= 1
        m_node = pre_m_node.next
        next_n_node = n_node.next
        
        
        
        
        
        
    def reverse(self, head):
        new_head = ListNode(0)
        p = head
        while p:
            t = p.next
            p.next = new_head.next
            new_head.next = p
            p = t
        return new_head.next

l = ListNode(1)
l.next = ListNode(2)
s = Solution()
t = s.reverse(l)
print t.val
print t.next.val
