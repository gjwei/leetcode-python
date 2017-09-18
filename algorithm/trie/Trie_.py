#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 8/31/17
  
"""


class TrieNode(object):
    def __init__(self, nodeChar):
        self.childNodes = [None for _ in range(26)]
        self.freq = 0
        self.nodeChar = nodeChar
        self.hash_set = set()
        
        
class Trie(object):
    
    def add_trie_node(self, root, word, word_id):
        """实现增加节点的操作
        
        Args:
            root: 上一层的节点
            word: 要插入的单词
            word_id: 插入单词的ID
        """
        if len(word) == 0:
            return
        k = ord(word[0]) - ord('a')
        if root.childNodes[k] is None:
            root.childNodes[k] = TrieNode(word[0])
        root.childNodes[k].hash_set.add(word_id)
        
        if len(word[1:]) == 0:
            root.childNodes[k].freq += 1
        self.add_trie_node(root.childNodes[k], word[1:], word_id)
        
    def delete_trie_node(self, root, word, word_id):
        """实现删除某个单词的操作，我们不仅要删除该节点的字符串编号，还要对词频进行减一操作
        Args:
            root: 正在访问的节点
            word: 要删除的单词
            word_id: 要删除单词的ID
            """
        if len(word) == 0:
            return
        # 计算字符的地址
        k = ord(word[0]) - ord('a')
        # 如果没有找到相应的字符，说明没有要找到的节点
        if root.childNodes[k] is None:
            return
        # 如果是最后一个字符，则减去字频
        if len(word) == 1 and root.childNodes[k].freq > 0:
            root.childNodes[k].freq -= 1
        root.childNodes[k].hash_set.remove(word_id)
        self.delete_trie_node(root.childNodes[k], word[1:], word_id)
        

if __name__ == '__main__':
    # 进行测试
    tire = Trie()
    
                
                
        