#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 9/10/17
  
"""

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here

        new_list = self.reverse(listNode)
        result = []
        while new_list:
            result.append(str(new_list.val))
            new_list = new_list.next
        print ''.join(result)


    def reverse(self, head):
        if not head or not head.next:
            return head
        new_head = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return new_head