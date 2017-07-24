class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        m = len(arrays)
        if m == 0 or m == 1:
            return 0
        
        
        left_index = 0 if arrays[0][0] <= arrays[1][0] else 1
        right_index = 0 if arrays[0][-1] >= arrays[1][-1] else 1
        left, left_second = arrays[left_index][0], arrays[1 - left_index][0]
        right, right_second = arrays[right_index][-1], arrays[1-right_index][-1]

        for i in xrange(m):
            if arrays[i][0] < left:
                left_second = left
                left = arrays[i][0]
                left_index = i
            if arrays[i][0] >= left and arrays[i][0] < left_second and left_index != i:
                left_second = arrays[i][0]
                
        for j in xrange(m):
            if arrays[j][-1] > right:
                right_second = right
                right = arrays[j][-1]
                right_index = j
            if arrays[j][-1] <= right and arrays[j][-1] > right_second and right_index != j:
                right_second = arrays[j][-1]
        if left_index != right_index:
            return abs(right - left)
        else:
            return max(right - left_second, right_second - left)
        
            
s = Solution()
a = [[-5,-2,0,1,1,2],[-7,-6,-3],[-8,-7,-4,-4,0,2,3,4]]

print s.maxDistance(a)