class Solution(object):
    
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        friends = range(len(M))
        n = len(M)
        for i in xrange(n):
            for j in xrange(i+1, n):
                if M[i][j] == 1:
                    self.union(friends, i, j)
        result = 0
        for i in xrange(len(friends)):
            if friends[i] == i:
                result += 1
        return result
    
    def union(self, father, x, y):
        fx = self.find(father, x)
        fy = self.find(father, y)
        if fx != fy:
            father[fx] = fy
                                    
    def find(self, father, x):
        if father[x] != x:
            father[x] = self.find(father, father[x])
        return father[x]
s = Solution()
a = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
print s.findCircleNum(a)