class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 0
        if n < 0:
            return self.myPow(1.0 / x, -n)
        if n == 0:
            return 1
        a = 1
        while n:
            if n & 1:
                a *= x
            x *= x
            n >>= 1
        return a
        
s = Solution()
print s.myPow(2, 5)