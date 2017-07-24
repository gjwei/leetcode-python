def cut_rod_dp(n, p):
    dp = [0 for _ in xrange(n + 1)]
    for i in xrange(1, n + 1):
        for j in xrange(i):
            dp[i] = max(dp[i], p[j] + dp[i - j])
    return dp[n]