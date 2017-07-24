def flatten(l):
    result = []
    for v in l:
        if isinstance(v, int):
            result.append(v)
        else:
            result += flatten(v)
    return result

t = flatten([1, 2, [3, 4, [5, 6]]])
print t