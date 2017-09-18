#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 9/15/17
  
"""

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
        
        
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        pHead = self.clone_nodes(pHead)
        pHead = self.connect_random(pHead)
        return self.seperate(pHead)
        
    def clone_nodes(self, head):
        p = head
        while p:
            t = p.next
            p.next = RandomListNode(p.label)
            p.next.next = t
            p = t
        return head
    
    def connect_random(self, head):
        p, q = head, head.next
        while p:
            if p.random:
                q.random = p.random.next
            p = p.next.next
            q = q.next.next
        return head
    
    def seperate(self, head):
        new_head = head.next
        p, q = head, new_head
        while p:
            p.next = q.next
            q.next = q.next.next
            p = p.next
            q = q.next
        return new_head
                
        
        
        