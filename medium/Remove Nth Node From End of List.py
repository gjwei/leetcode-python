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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        new_head = ListNode(0)
        new_head.next = head
        left, right = new_head, new_head
        while n + 1:
            right = right.next
            n -= 1
        while right:
            right = right.next
            left = left.next
        left.next = left.next.next
        return new_head.next

    