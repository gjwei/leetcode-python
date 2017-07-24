#coding: utf-8

def merge_sort(a):
    if len(a) == 1:
        return a
    if len(a) == 2:
        a[0], a[1] = min(a), max(a)
        return a
    left_part = merge_sort(a[: len(a)//2])
    right_part = merge_sort(a[len(a)//2 :])

    result = merge(left_part, right_part)
    return result

def merge(left, right):
    result = [0 for _ in xrange(len(left) + len(right))]
    index = 0
    left_index, right_index = 0, 0
    while left_index < len(left) or right_index < len(right):
        if left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                result[index] = left[left_index]
                left_index += 1
            else:
                result[index] = right[right_index]
                right_index += 1
        elif left_index < len(left):
            result[index] = left[left_index]
            left_index += 1
        else:
            result[index] = right[right_index]
            right_index += 1
        index += 1
    return result

a = [3, 2 ,6, 4, 1, 4, 7]
print merge_sort(a)
