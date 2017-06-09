# coding: utf-8
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return self.find_boundary(nums, target)
    
    def find_boundary(self, nums, target):
        result = [-1, -1]
        left, right = 0, len(nums) - 1
        mid = (left + right) // 2
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[left] != target:
            return result
        result[0] = left

        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2 + 1
            if nums[mid] > target:
                j = mid - 1
            else: 
                i = mid
        result[1] = j
        return result

                
        

s = Solution()
print s.searchRange([5, 7, 7, 8, 8, 10], 8)  
                