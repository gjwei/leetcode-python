class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """  
        result = 0
        for i in xrange(len(points)):
            d = dict()
            for j in xrange(0, len(points)):
                if i == j:
                    continue
                distance = self.get_distance(points[i], points[j])
                d[distance] = d.get(distance, 0) + 1
            for _, value in d.iteritems():
                result += (value) * (value - 1)
        return result
        
    def get_distance(self, x, y):
        return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2

s = Solution()
print s.numberOfBoomerangs([[0,0],[1,0],[2,0]])