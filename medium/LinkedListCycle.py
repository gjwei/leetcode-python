#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 3/26/17
  
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from ListNode import *

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while slow and fast:
            slow = slow.next
            fast = fast.next
            if fast.next:
                fast = fast.next
            else:
                return False
            if slow == fast:
                return True
        return False


    