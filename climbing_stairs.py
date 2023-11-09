def climbStairs(self, n):
    if n == 0:
        n = 0
    if n == 1:
        n = 1
    if n == 2:
        n = 2

    dp = [0] * (n + 1)

    dp[1] = 1
    dp[2] = 1

    for i in range(3, n + 1): # n+ 1 because its exclusive
        dp[i] = dp[i] + dp[i - 1]

    return dp[n]