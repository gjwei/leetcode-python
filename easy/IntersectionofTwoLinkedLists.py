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
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1, p2 = headA, headB
        sizeA, sizeB = 0, 0
        while p1:
            sizeA += 1
            p1 = p1.next
        while p2:
            sizeB += 1
            p2 = p2.next
        p1, p2 = headA, headB
        size_diff = abs(sizeA - sizeB)
        if sizeA > sizeB:
            while size_diff:
                p1 = p1.next
                size_diff -= 1
        else:
            while size_diff:
                p2 = p2.next
                size_diff -= 1
        while p1 and p2:
            if p1 != p2:
                p1 = p1.next
                p2 = p2.next
            else:
                return p1


    