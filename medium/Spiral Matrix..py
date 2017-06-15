class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # m, n = len(matrix), len(matrix[0])
    
        

        # visited = [[False for _ in xrange(n)] for _ in xrange(m)]
        # i, j = 0, 0
        # result = [matrix[0][0]]
        # visited[0][0] = True
        # while len(result) < m * n:
        #     while j + 1 < n and not visited[i][j + 1] :
        #         result.append(matrix[i][j + 1])
        #         visited[i][j + 1] = True
        #         j = j + 1
        #     while i+ 1 < m and not visited[i + 1][j]:
        #         result.append(matrix[i + 1][j])
        #         visited[i + 1][j] = True
        #         i = i + 1
        #     while j - 1 >= 0 and not visited[i][j - 1]:
        #         result.append(matrix[i][j - 1])
        #         visited[i][j - 1] = True
        #         j = j - 1
        #     while i - 1 >= 0 and not visited[i - 1][j]:
        #         result.append(matrix[i - 1][j])
        #         visited[i - 1][j] = True
        #         i = i - 1
        # return result
    
    def recurisive(self, matrix, result):
        print matrix
        if len(matrix) == 0:
            return result
        #
        m, n = len(matrix), len(matrix[0])
        for i in xrange(n):
            result.append(matrix[0][i])
        for i in xrange(1, m):
            result.append(matrix[i][-1])
        for i in xrange(2, n + 1):
            result.append(matrix[m - 1][-i])
        for i in xrange(2, m + 1):
            result.append(matrix[-i][0])
        return self.recurisive(matrix[1:m - 1][1:n - 1], result)


            
                




m = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
s = Solution()
print s.recurisive(m, [])