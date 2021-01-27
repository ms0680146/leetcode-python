'''
Solution: Dynamic Programming

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

init: dp[0] = 1, dp[1] = 1, dp[2] = 2
dp[i] = dp[i-1] + dp[i-2]
'''
def climbStairs(n):
    dp = [1, 1]
    for i in range(2, n): # 2
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]

print(climbStairs(3)) # 3