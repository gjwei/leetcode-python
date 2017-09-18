#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
 created by gjwei on 7/30/17
  
"""
"""对一组二维的坐标求解最近的两点的距离
"""
def get_min_distance(points):
    '''
    
    :param points: 点的坐标(x, y)
    :return min_distance: 最小的距离 int
    '''
    if len(points) == 0 or len(points) == 1:
        return 1 << 31
    
def _get_min_distance(points, left_point, right_point):
    '''
    
    :param points:
    :param left_points:
    :param right_points:
    :return:
    '''
    if len(points) == 1:
        return 1 << 31
    if len(points) == 2:
        return distance(points[0], points[1])
    mid_x = (left_point[0] + right_point[0]) >> 1
    left_points, right_points = [], []
    mid_left, mid_right = left_point, right_point
    for point in points:
        if point[0] <= mid_x:
            left_points.append(point)
            if mid_x - point[0] < mid_x - mid_left[0]:
                mid_left = point
        else:
            right_points.append(point)
            if point[0] - mid_x < mid_right[0] - mid_x:
                mid_right = point
    mid_min_distance = distance(mid_left, mid_right)
    return min(_get_min_distance(left_points, left_point, mid_left), _get_min_distance(right_points, right_point, mid_right))

       
def distance(point1, point2):
    return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2