#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 3/26/17
  
"""

from ListNode import *
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        while p and p.next:
            if p.next.val == p.val:
                p.next = p.next.next
            else:
                p = p.next
        return head


    