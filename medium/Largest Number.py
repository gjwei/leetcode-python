#coding: utf-8
"""思路：将数组按照一定规则进行排序，之后将排序后的数组拼接成字符串即可"""

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        def cmp(a, b):
            a, b = str(a), str(b)
            if a[0] > b[0]:
                return 1
            elif a[0] < b[0]:
                return -1
            else:
                a_next, b_next = a[0], b[0]
                for i, c in enumerate(a):
                    if i > 0 and a[i] != a[0]:
                        a_next = c
                        break
                for i, c in enumerate(b):
                    if i > 0 and b[i] != b[0]:
                        b_next = b[i]
                
                    
    
    