#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 9/14/17
  
"""


class DListNode(object):
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.previous, self.next = None, None
        

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head, self.end = None, None
        self.current_capacity = 0
        self.max_capacity = capacity
        self.hash_dict = {}
    
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hash_dict:
            res = self.hash_dict[key]
            # move to first
            self.move_head(res)
            return res.val
        else:
            return -1
    
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # node = DListNode(key, value)
        if self.head is None or self.max_capacity == 1:
            self.head = self.end = DListNode(key, value)
            self.hash_dict[key] = self.head
            self.current_capacity = 1
            return
        
        if key in self.hash_dict:
            # 已经存在，更新
            p = self.hash_dict[key]
            if p.previous is None:
                # p is head
                return
            elif p.next is None:
                # p is end
                self.end = p.previous
                p.previous = None
                self.end.next = None
            else:
                p.previous.next = p.next
                p.next.previous = p.previous
                p.previous = None
                
            p.next = self.head
            self.head.previous = p
            self.head = p
            return
        else:
            # add a new node
            node = DListNode(key, value)
            self.hash_dict[key] = node
            
            if self.current_capacity == self.max_capacity:
                # 超出容量, 去除末尾的元素
                self.hash_dict.pop(self.end.key)
                self.end = self.end.previous
                self.end.next = None
                
            node.next = self.head
            self.head.previous = node
            self.head = node
            self.current_capacity += 1
            return
            
                
                
        
        
    def move_head(self, node):
        """Move node to head"""
        if node.next is None:
            self.end = node.previous
            self.end = None
            
            node.previous = None
            node.next = self.head
            self.head.previous = node
            self.head = node
        elif node.previous is None:
            return
        else:
            # move to first
            node.previous.next = node.next
            node.next.previous = node.previous
            node.previous = None
            
            node.next = self.head
            self.head.previous = node
            self.head = node
    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    cache.put(4, 4)
    
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))
    

