# coding: utf-8
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # return self.find_boundary(nums, target)
        #divide and Conque 
        # def search(left, right):
        #     if nums[left] == target == nums[right]:
        #         return [left, right]
        #     if nums[left] <= target <= nums[right]:
        #         mid = (left + right) >> 1
        #         l, r = search(left, mid), search(mid + 1, right)
        #         return max(l, r) if -1 in l + r else [l[0], r[1]]
        #     return [-1, -1]
        # return search(0, len(nums) - 1)

        def search(n):
            lo, hi = 0, len(nums) - 1
            while lo < hi:
                mid = (lo + hi) >> 1
                if nums[mid] < n:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        
        left = search(target)
        if nums[left] != target:
            return [-1, -1]
        right = search(target + 1) - 1
        return [left, right]

    
    # def find_boundary(self, nums, target):
    #     result = [-1, -1]
    #     left, right = 0, len(nums) - 1
    #     mid = (left + right) // 2
    #     while left < right:
    #         mid = (left + right) // 2
    #         if nums[mid] < target:
    #             left = mid + 1
    #         else:
    #             right = mid
    #     if nums[left] != target:
    #         return result
    #     result[0] = left

    #     right = len(nums) - 1
    #     while left < right:
    #         mid = (left + right) // 2 + 1
    #         if nums[mid] > target:
    #             j = mid - 1
    #         else: 
    #             i = mid
    #     result[1] = j
    #     return result

                
        

s = Solution()
print s.searchRange([5, 7, 7, 8, 8, 10], 8)  
                