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
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverseList(head, None)

    def reverse_list(self, head, new_head):
        if not head:
            return new_head
        next = head.next
        head.next = new_head
        return self.reverse_list(next, head)




    