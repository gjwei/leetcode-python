class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        is_prime = [True for i in xrange(n)]
        result = 0
        for i in xrange(2, n):
            if is_prime[i]:
                result += 1
                for j in xrange(2, n // i):
                    is_prime[i * j] = False
        return result
