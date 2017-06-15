#coding: utf-8
#回溯法
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return [[]]
        result = []
        for i in xrange(1, n + 1):
            pres = self.combine(i - 1, k - 1)
            for pre in pres:
                result.append(pre + [i])
        return result

