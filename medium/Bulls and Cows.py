class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        d = [0 for _ in xrange(10)]
        a, b = 0, 0
        for i, c in enumerate(secret):
            d[ord(c) - ord('0')] += 1
            if c == guess[i]:
                a += 1
        for c in guess:
            if d[ord(c) - ord('0')] > 0:
                b += 1
                d[ord(c) - ord('0')] -= 1
        return str(a) + 'A' + str(b - a) + 'B'

s = Solution()
print s.getHint('1123', '0111')
