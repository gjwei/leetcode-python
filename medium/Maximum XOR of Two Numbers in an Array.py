class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m, mask = 0, 0
        for i in xrange(31, -1, -1):
            mask |= (1 << i)
            s = set()
            for n in nums:
                s.add(n & mask)
            tmp = m | (1 << i)
            for prefix in s:
                if tmp ^ prefix in s:
                    m = tmp
                    break
        return m