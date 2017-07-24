class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        self.maxdays = max(v[1] for v in courses)        
        self.result = 0
        is_taken = [False for _ in xrange(len(courses))]
        self.dfs(courses, is_taken, 0, 0)
        return self.result
            
    def dfs(self, courses, is_taken, count, days):
        
        if days > self.maxdays or sum(is_taken) == len(is_taken):
            return
        self.result = max(self.result, count)
        for i in xrange(len(courses)):
            if not is_taken[i] and days + courses[i][0] <= courses[i][1]:
                # print i
                is_taken[i] = True
                self.dfs(courses, is_taken, count + 1, days + courses[i][0])
                is_taken[i] = False
            

        
        
        
a = [[914,9927],[333,712],[163,5455],[835,5040],[905,8433],[417,8249],[921,9553],[913,7394],[303,7525],[582,8658],[86,957],[40,9152],[600,6941],[466,5775],[718,8485],[34,3903],[380,9996],[316,7755]]
s = Solution()
print s.scheduleCourse(a)