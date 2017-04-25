#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 3/27/17
  
"""
from ListNode import *

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1, p2 = l1, l2
        p = head = ListNode(0)
        while p1 and p2:
            if p1.val > p2.val:
                p.next = p2
                p2 = p2.next
            else:
                p.next = p1
                p1 = p1.next
            p = p.next
        while p1:
            p.next = p1
            p1 = p1.next
            p = p.next
        while p2:
            p.next = p2
            p2 = p2.next
            p = p.next
        return head.next


    