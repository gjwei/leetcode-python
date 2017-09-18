#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 8/25/17
  
"""
RED, BLACK = True, False

class Node(object):
    def __init__(self, val, num, key):
        self.key = key
        self.val = val
        self.left, self.right = None, None
        self.num = num
        self.color = False

class RedBlackTree(object):
    
    def is_red(self, node):
        """判断节点是否是红色连接
        Args:
            node: 要判断的节点
            """
        if node is None:
            return False
        return node.color == RED
    
    def rotate_left(self, node):
        """实现红色链接的坐旋转"""
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = RED
        x.num = node.num
        node.num = 1 + self.size(node.left) + self.size(node.right)
        return x
    
    def rotate_right(self, node):
        """实现node节点的右旋转"""
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = x.color
        x.num = node.num
        node.num = 1 + self.size(node.left) + self.size(node.right)
        return x
    
    def size(self, node):
        if node is None:
            return 0
        return node.num
    
    def put(self, key, val):
        root = self._put(self.root, key, val)
        self.root.color = BLACK
        
    def _put(self, h, key, val):
        if h is None:
            return Node(key, val, 1, RED)
        c = cmp(key, h.key)
        if c < 0:
            h.left = self._put(h.left, key, val)
        elif c > 0:
            h.right = self._put(h.right, key, val)
        else:
            h.val = val
            
        if self.is_red(h.right)  and (not self.is_red(h.left)):
            h = self.rotate_left(h)
        if self.is_red(h.left) and self.is_red(h.left.left):
            h = self.rotate_right(h)
        if self.is_red(h.left) and self.is_red(h.right):
            self.flip_color(h)
        h.num = self.size(h.left) + self.size(h.righ) + 1
        return h
    
    def flip_color(self, h):
        if h is None:
            return
        h.color = RED
        if h.left is not None:
            h.left.color = BLACK
        if h.right is not None:
            h.right.color = BLACK
        return
    
      
            
        
        
        
    
        
        
    
     