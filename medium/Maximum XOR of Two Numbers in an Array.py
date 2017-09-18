class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m, mask = 0, 0
        for i in range(31, -1, -1):
            mask |= (1 << i)
            s = set()
            for n in nums:
                s.add(n & mask)  # reserve left bits and ignore right bits
            """ use 0 to keep the bit, 1 to find XOR
            """
            tmp = m | (1 << i)
            for prefix in s:
                if tmp ^ prefix in s:
                    m = tmp
                    break
        return m