class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        stack = []
        result = []
        for n in nums:
            while stack and stack[-1] < n:
                d[stack.pop()] = x
            stack.append(n)
        for x in findNums:
            result.append(d.get(x, -1))
        return result