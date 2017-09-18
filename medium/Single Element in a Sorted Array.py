#coding: utf-8
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) >> 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid * 2] != nums[mid * 2 + 1]:
                right = mid
            else:
                left = mid + 1
        # left, right = 0, len(nums) - 1
        # while left < right:
        #     print left, right
        #     mid = (left + right) >> 1
        #     if nums[mid] == nums[mid + 1]:
        #         mid -= 1
        #     left_count = mid - left + 1
        #     if left_count & 1 == 0:
        #         left = mid + 1
        #     else:
        #         right = mid
        # return nums[left]
        #
                
s = Solution()

a = [3,3,7,7,10,11,11]
print s.singleNonDuplicate(a)