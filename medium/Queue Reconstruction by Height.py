#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 7/27/17
  
"""


class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # result = []
        # people = sorted(people, key=lambda x: x[0])
        # visited = [False for _ in xrange(len(people))]
        # while len(result) < len(people):
        #     for i in xrange(len(people)):
        #         if not visited[i]:
        #             count = 0
        #             for j in xrange(len(result)):
        #                 if people[i][0] <= result[j][0]:
        #                     count += 1
        #             if count == people[i][1]:
        #                 result.append(people[i])
        #                 visited[i] = True
        #                 break
        # return result
        people = sorted(people, cmp=lambda x1, x2: x2[0] - x1[0] if x1[0] != x2[0] else x1[1] - x2[1])
        result = []
        for p in people:
            result.insert(p[1], p)
        return result
        
        
s = Solution()
a = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

print s.reconstructQueue(a)
            
            

