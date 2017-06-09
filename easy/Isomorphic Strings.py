class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(t) != len(s):
            return False
        d_s = [-1 for _ in xrange(256)]
        d_t = [-1 for _ in xrange(256)]
        s_index = range(len(s))
        t_index = range(len(t))
        for i in xrange(len(s)):
            if d_s[ord(s[i])] == -1:
                d_s[ord(s[i])] = i
            else:
                s_index[i] = d_s[ord(s[i])]
            if d_t[ord(t[i])] == -1:
                d_t[ord(t[i])] = i
            else:
                t_index[i] = d_t[ord(t[i])]
        for i in xrange(len(s)):
            if s_index[i] != t_index[i]:
                return False
        print s_index
        print t_index
        return True
s = Solution()
print s.isIsomorphic('ab', 'aa')

