# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key=lambda x: x[0])
        # print intervals
        result = []
        for i, l in enumerate(intervals):
            if i == 0:
                result.append(l)
            else:
                t = result[-1]
                if t[0] <= l[0] <= t[1]:
                    result[-1][1] = max(t[1], l[1])
                else:
                    result.append(l)
        return result

a = [[1,3],[8,10],[2,6],[15,18]]
s = Solution()
result = s.merge(a)
print result