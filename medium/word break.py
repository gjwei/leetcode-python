class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        d = set(wordDict)
        if len(s) == 1:
            return s in d
        h = [False for _ in xrange(len(s)+1)]
        h[0] = True
        for i in xrange(1, len(s)+1):
            for j in xrange(i):
                h[i] = h[i] or (h[j] and s[j:i] in d)
        print h
        return h[len(s)]
            
s = Solution()
a = "aaaaaaa"
d = ["aaaa","aaa"]
print s.wordBreak(a, d)