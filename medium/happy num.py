class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nums = set()
        while n != 1:
            print n
            if n in nums:
                return False
            nums.add(n)
            n = self.get_next_num(n)
        return True
        
    def get_next_num(self, n):
        result = 0
        while n:
            result = result + (n % 10) ** 2
            n /= 10
        return result
s = Solution()
print s.isHappy(2)