class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums_dict = {}
        for i in nums:
            nums_dict[i] = nums_dict.get(i, 0) + 1
        count = 0
        for key in nums_dict.keys():
            if k > 0 and key + k in nums_dict:
                count += 1
            elif k == 0:
                count = count + 1 if nums_dict[key] > 1 else count = count
        return count

