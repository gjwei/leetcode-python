import string
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        t = ord('a') - ord('A')
        left, right = 0, len(s) - 1
        alphanumeric = string.ascii_letters + string.digits
        while left < right:
            if s[left] not in alphanumeric:
                left += 1
                continue
            if s[right] not in alphanumeric:
                right -= 1
                continue
            if s[left] == s[right] or (s[left] in string.ascii_letters and s[right] in string.ascii_letters and (ord(s[left]) + t == ord(s[right]) or ord(s[left]) - t == ord(s[right]))):
                left += 1
                right -= 1
            else:
                return False
        return True
                

s = Solution()
print s.isPalindrome("A man, a plan, a canal: Panama")   
        