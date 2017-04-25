#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 3/27/17
  
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p, slow, fast = head, head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow

    def reverse(self, head):
        if not head:
            return None
        new_head = head.next
        head.next = None
        while new_head:


    