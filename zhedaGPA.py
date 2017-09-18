#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 8/27/17
  
"""
weight = [1] + [2] * 9
grades = [74, 92, 81, 79, 85, 94, 78, 89, 82, 83]

def calculate_single_course(grade):
    if grade >= 85:
        return 4.0
    else:
        return 1.5 + (grade - 60) * 0.1

if __name__ == '__main__':
    grades = [calculate_single_course(grade) for grade in grades]
    print grades
    result = sum([weight[i] * grades[i] for i in xrange(len(weight))]) * 1.0 / sum(weight)
    print result



