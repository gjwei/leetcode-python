'''
Find all possible combinations of k numbers that add up
to a number n, given that only numbers from 1 to 9 can be used
and each combination should be a unique set of numbers.
'''

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(n, k, result, [], 0, 1)
        return result

    def dfs(self, n, k, result, l, l_sum, last):
        if len(l) > k or l_sum > n:
            return
        if len(l) == k and l_sum == n:
            result.append(l[:])
        for i in xrange(last, 10):
            l.append(i)
            l_sum += i
            self.dfs(n, k, result, l, l_sum, i + 1)
            l_sum -= i
            l.pop()

s = Solution()
print s.combinationSum3(3, 9)


