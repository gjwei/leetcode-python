class Solution(object):
    def smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
        result = []
        if a == 1:
            return 1
        flag = self._smallestFactorization(a, result)
        if not flag:
            return 0
        else:
            return int(''.join(sorted(result)))
    
    def _smallestFactorization(self,a, result):
        if a == 1:
            return True
        flag = False
        for i in range(2, 10)[::-1]:
            j = i
            if a % j == 0:
                result.append(str(j))
                flag = flag or self._smallestFactorization(a / j, result)
        return flag
        
s = Solution()
print s.smallestFactorization(48)
