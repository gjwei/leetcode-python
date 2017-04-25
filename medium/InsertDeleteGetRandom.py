#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data_list = []
        self.data_dict = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.data_dict:
            self.data_dict[val] = len(self.data_list)
            self.data_list.append(val)
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.data_dict:
            index, last_data = self.data_dict[val], self.data_list[-1]
            self.data_list[index] = last_data
            self.data_dict[last_data] = index  # update last_data position
            self.data_list.pop()  # remove the last data
            self.data_dict.pop(val)  # remove val in dict

            return True
        return False

    """
    if val in self.pos:
            idx, last = self.pos[val], self.nums[-1]
            self.nums[idx], self.pos[last] = last, idx
            self.nums.pop(); self.pos.pop(val, 0)
            return True
        return False
    """

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.data_list)


