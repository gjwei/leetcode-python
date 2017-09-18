import re

class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        nums = map(int, re.findall('[+-]?\d+', expression))
        print nums
        index = 0
        A, B = 0, 1
        while index < len(nums):
            a = nums[index]
            b = nums[index + 1]
            index += 2
            A = A * b + a * B
            B *= b
            t = self.gcd(A, B)
            A //= t
            B //= t
        return '%d/%d' % (A, B)
    
    def gcd(self, a, b):
        return a if b == 0 else self.gcd(b, a % b)

s = Solution()
print s.fractionAddition("1/3-1/2")
        
