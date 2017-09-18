#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 9/10/17
  
"""

"""我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共
有多少种方法"""

# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        """
        解题的思路：
            因为砖块的大小为2x1，所以砖块最大的影响范围是2
            所以，n的排列只和n-1，n-2相关
            题目就转化成斐波那契数列问题。
        :param number:
        :return:
        """