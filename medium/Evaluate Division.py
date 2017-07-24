class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        d = {}
        for i in xrange(len(equations)):
            if values[i] == 0:
                d[equations[i][0]] = 0
            elif equations[i][0] in d:
                d[equations[i][1]] = d[equations[i][0]] / values[i]
            elif equations[i][1] in d:
                d[equations[i][0]] = values[i] * d[equations[i][1]]
            else:
                d[equations[i][1]] = 1.0
                d[equations[i][0]] = values[i]
        result = []
        print d
        for i in xrange(len(queries)):
            if queries[i][0] not in d or queries[i][1] not in d or d[queries[i][1]] == 0:
                result.append(-1.0)
            else:
                result.append(d[queries[i][0]] / d[queries[i][1]])
        return result
s = Solution()
e = [["a","b"],["e","f"],["b","e"]]
v = [3.4,1.4,2.3]
q = [["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"]]

print s.calcEquation(e, v, q)