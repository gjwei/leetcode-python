class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        result = [nums[0]]
        l = len(result)
        for v in nums[1:]:
            index_v = self.upper(result, v, 0, len(result) - 1)
            print index_v
            if index_v == len(result):
                result.append(v)
            else:
                result[index_v] = v
            l = max(l, index_v + 1)
        return l
            
        
    def upper(self, r, v, left, right):
        if v > r[right]:
            return right + 1
        if v < r[left]:
            return left
        mid = (left + right) >> 1
        if r[mid] > v:
            return self.upper(r, v, left, mid - 1)
        elif r[mid] == v:
            return mid
        else:
            return self.upper(r, v, mid + 1, right)
    
a = [10,9,2,5,3,7,101,18]
s = Solution()
print s.lengthOfLIS(a)