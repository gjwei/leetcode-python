import sys

def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0 for _ in xrange(n+1)] for _ in xrange(n+1)]
    s = [[0 for _ in xrange(n+1)] for _ in xrange(n+1)]
    for l in xrange(2, n+1):
        for i in xrange(1, n - l + 1):
            j = i + l - 1
            m[i][j] = 2 << 30 - 1
            for  k in xrange(i, j):
                q  = m[i][k] + m[k + 1][j] + p[i - 1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s


    