#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 3/29/17
  
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
        :rtype: 
        """
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        p = slow.next
        slow.next = None
        right_part = self.reverse_list(p)
        while right_part and head:
            if p.val != head.val:
                return False
        return True


    def reverse_list(self, head):
        """reverse the list"""
        p = head
        t = None
        new_head = p
        while p:
            q = p.next
            p.next = t
            new_head = p
            p, t = q, p
        return new_head


    def reverse_list_recursive(self, head, new_head):
        if head == None:
            return new_head
        p = head.next
        head.next = new_head
        return self.reverse_list_recursive(p, head)


        
a = ListNode(1)
a.next = ListNode(2)
# a.next.next = ListNode(3)
s = Solution()

u = s.reverse_list(a)
print u.val, u.next.val
    










    