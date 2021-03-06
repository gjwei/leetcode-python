#coding: utf-8
"""一种双核CPU的两个核能够同时的处理任务，现在有n个已知数据量的任务需要交给CPU处理，假设已知CPU的每个核1秒可以处理1kb，每个核同时只能处理一项任务。n个任务可以按照任意顺序放入CPU进行处理，现在需要设计一个方案让CPU处理完这批任务所需的时间最少，求这个最小的时间。 
输入描述:
输入包括两行：
第一行为整数n(1 ≤ n ≤ 50)
第二行为n个整数length[i](1024 ≤ length[i] ≤ 4194304)，表示每个任务的长度为length[i]kb，每个数均为1024的倍数。
"""
import sys


class Solution(object):
    def get_min_time(self, a):
        if len(a) == 0:
            return 0
        a = sorted(a)
        left, right = 0, len(a) - 1
        left_sum, right_sum = a[0], a[-1]
        while left < right:
            if left_sum == right_sum:
                left += 1
                left_sum += a[left]
            elif left_sum < right_sum:
                left += 1
                left_sum += a[left]
            else:     
                right -= 1
                right_sum += a[right]
        return max(left_sum, right_sum)


if __name__ == '__main__':
    a = [3072, 3072, 7168, 3072, 1024]
    s = Solution()
    print s.get_min_time(a)
