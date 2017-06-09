#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 6/2/17
  
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        for i in xrange(len(s)):
            palindrome_of_odd = self.get_length_of_Palindrome(s, i, i)
            palindrome_of_even = ''
            if i < len(s) - 1:
                palindrome_of_even = self.get_length_of_Palindrome(s, i, i + 1)
            if len(palindrome_of_even) > len(palindrome_of_odd) and len(palindrome_of_even) > len(result):
                result = palindrome_of_even
            elif len(palindrome_of_odd) > len(palindrome_of_even) and len(palindrome_of_odd) > len(result):
                result = palindrome_of_odd
        return result

    def get_length_of_Palindrome(selfs, s, left, right):
        if s[left] != s[right]:
            return s[left]
        else:
            result = s[left:right+1]
        while left >= 0 and right < len(s):
            if (s[left] != s[right]):
                break
            else:
                result = s[left: right+1]
                right += 1
                left -= 1
        return result

s = Solution()
print s.longestPalindrome("a")