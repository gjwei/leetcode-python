class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0 for _ in xrange(num + 1)]
        result[1] = 1
        for i in xrange(2, num + 1):
            if not i & 1:
                result[i] = result[i >> 1]
            else:
                result[i] = result[i - 1] + 1
        return result

s = Solution()
print s.countBits(6)