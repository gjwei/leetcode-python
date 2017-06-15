class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # result = []
        # for i in xrange(4):
        #     for j in xrange(i + 1, i + 4):
        #         for k in xrange(j + 1, j + 4):
        #             a, b, c, d = s[:i], s[i:j], s[j:k], s[k:]
        #             if self.is_valid(a) and self.is_valid(b) and self.is_valid(c) and self.is_valid(d):
        #                 result.append('.'.join([a, b, c, d]))
        # return result
        result = []
        nums = []
        self.dfs(s, result, nums, 0)
        return result


    def dfs(self, s, result, nums, index):
        if len(nums) > 4:
            return
        if len(nums) == 4:
            if index >= len(nums):
                result.append('.'.join(nums))
            return
        for i in xrange(1, 4):
            if index + i > len(s):
                break
            n = s[index:index+i]
            if self.is_valid(n):
                nums.append(n)
                self.dfs(s, result, nums, index + i)
                nums.pop()
            else:
                break                
  
    def is_valid(self, num):
        if len(num) == 0 or str(int(num)) != num or int(num) > 255:
            return False
        else:
            return True

s = Solution()
print s.restoreIpAddresses("25525511135")