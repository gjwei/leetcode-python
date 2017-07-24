def memoized_cut_rod(n):
    r = [-1 for _ in xrange(n + 1)]
    return _memoized_cut_rod_aux(p, n, r)

def _memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -1
        for i in xrange(1, n + 1):
            q = max(q, p[i]+_memoized_cut_rod_aux(p, n - i, r))
    r[n] = q
    return q