#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Created by gjwei on 2016/12/23
 
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
        p1 = l1
        p2 = l2
        s1 = []
        s2 = []
        while(p1):
            s1.append(p1.val)
            p1 = p1.next
        while(p2):
            s2.append(p2.val)
            p2 = p2.next
        result = []
        carry = 0
        while(len(s1) != 0 and len(s2) != 0):
            t1 = s1.pop()
            t2 = s2.pop()
            carry = (t1 + t2 + carry) / 10
            result.append((t1 + t2 + carry) % 10)
        while(len(s1)):
            t1 = s1.pop()
            carry = (t1 + carry) / 10
            result.append((t1 + carry) % 10)
        while(len(s2)):
            t2 = s2.pop()
            carry = (t2 + carry) / 10
            result.append((t2 + carry) % 10)
        if(carry > 0):
            result.append(carry)
        out = ListNode(0)
        p = out
        while(len(result)):
            t = result.pop()
            p.next = ListNode(t)
            p = p.next
        return out.next

