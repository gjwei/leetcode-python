#coding: utf-8
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return mid
            if (mid - left + 1) & 1 == 0:
                if nums[mid] == nums[mid + 1]: #in left
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] == nums[mid + 1]:
                    left = mid
                else:
                    right = mid

            return nums[right]
                
        # if len(nums) == 1:
        #     return nums[0]
        # if nums[0] != nums[1]:
        #     return nums[0]
        # if nums[-1] != nums[-2]:
        #     return nums[-1]
        # mid = len(nums) >> 1
        # if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
        #     return nums[mid]
        # elif mid & 1 == 1 and nums[mid] == nums[mid - 1]:
        #     return self.singleNonDuplicate(nums[mid + 1:])
        # elif mid & 1 == 1 and num[mid] != nums[mid - 1]:
        #     pass
s = Solution()

a = [1, 1, 3, 3, 2,  5, 5]
print s.singleNonDuplicate(a)