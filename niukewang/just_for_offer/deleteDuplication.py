#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 9/16/17
  
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
        
class Solution:
    
    def deleteDuplication(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead
        head = ListNode(0) if pHead.val != 0 else ListNode(-1)
        p, q, q_pre = head, head.next, head
        while p and q and q.next:
            if q.val != q.next.val:
                if q.val == q_pre.val:
                    q_pre = q
                    q = q.next
                p = q
                q_pre = q
                q = q.next
            else:
                q_pre = q
                q = q.next
        return head.next
        
        
        
        
            
            
        
