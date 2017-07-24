# coding: utf-8
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        d = dict(zip(intervals, range(len(intervals))))
        intervals_sorted = sorted(intervals, key=lambda x: x.start)
        result = []
        for v in intervals:
            get_right = self.bs(intervals_sorted, v.end)
            if get_right:
                result.append(d[get_right])
            else:
                result.append(-1)
        return result
                
        
    def bs(self, intervals, end):
        #找到一个interval，使得它的start > 参数end
        left, right = 0, len(intervals) - 1
        while left <= right:
            if end <= intervals[left].start:
                return intervals[left]
            mid = (left + right) >> 1
            if intervals[mid].start < end:
                left = mid + 1
            else:
                right = mid
        return None
                
    
a = []
a.append(Interval(3, 4))
a.append(Interval(2,3))
a.append(Interval(1,2))
s = Solution()

print s.findRightInterval(a)
