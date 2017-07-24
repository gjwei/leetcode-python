#coding: utf-8
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [i + 1 for i in xrange(n)]    

        is_visited = [False for _ in xrange(n)]
        result = self.get_kth_permutation(is_visited, k, '', n)
        return result
    
    
    def get_kth_permutation(self, is_visited, k, current_str, n, result):
        if k == 0:
            result = current_str
            return
        for i in xrange(n):
            if not is_visited[i]:
                is_visited[i] = True
                self.get_kth_permutation(is_visited, k, current_str + str(i + 1), n)
                is_visited[i] = False
    
    
s = Solution()
print s.getPermutation(3, 1)    