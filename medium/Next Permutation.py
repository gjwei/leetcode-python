#coding: utf-8
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #1. 从后往前找到第一个非增位置，如果该位置为0，则说明该序列为递减序列
        #2. 从后往前找到第一个大于步骤一位置的数字，这个是要进行交换的数字
        #3. 将#1位置后的数字全部翻转
        #1
        p = len(nums) - 1
        while p > 0:
            if nums[p - 1] >= nums[p]:
                p -= 1
            else:
                break
        print p
        q = len(nums) - 1
        while  q >= p:
            if nums[q] > nums[p - 1]:
                break
            else:
                q -= 1
        nums[p - 1], nums[q] = nums[q], nums[p - 1]
        print q
        q = len(nums) - 1
        while p < q:
            nums[p], nums[q] = nums[q], nums[p]
            p += 1
            q -= 1

a = [1, 2, 1, 5, 4, 3, 3, 2, 1]
s = Solution()
s.nextPermutation(a)
print a

         

        
