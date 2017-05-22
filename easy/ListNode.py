#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 3/26/17
  
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


a = ListNode(1)
a.next = ListNode(3)

a.next = None
print a.val
print a.next


def main():
    print "hello"
    a = []
    for i in range(20):
        a.append(i)

    return a
