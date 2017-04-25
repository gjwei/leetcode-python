#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Created by gjwei on 2017/3/8
  
"""

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if len(timeSeries) == 0:
            return 0
        if len(timeSeries) == 1:
            return duration
        result = 0
        for i in xrange(len(timeSeries)):
            if i < len(timeSeries) - 1:
                if timeSeries[i + 1] >= timeSeries[i] + duration:
                    result += duration
                else:
                    result += (timeSeries[i+1] - timeSeries[i])
            else:
                result += min(duration, timeSeries[i] - timeSeries[i - 1])
        return result




