#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Created by gjwei on 2016/12/14
 
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        result = ListNode(0)
        p = result
        while(l1 and l2):
            current= l1.val + l2.val + carry
            (current, carry) = (current % 10, current / 10)
            p.next = ListNode(current)
            l1 = l1.next
            l2 = l2.next
            p = p.next
        #l1没到头
        while l1:
            current = l1.val + carry
            current, carry = current % 10, current / 10
            p.next = ListNode(current)
            l1 = l1.next
            p = p.next
        #l2没到头
        while l2:
            current = l2.val + carry
            current, carry = current % 10, current / 10
            p.next = ListNode(current)
            l2 = l2.next
            p = p.next
        if carry:
            p.next = ListNode(carry)
            p = p.next
        return result.next