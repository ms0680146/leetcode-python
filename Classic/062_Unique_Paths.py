'''
Solution: Dynamic Programming

Input: m = 3, n = 7
Output: 28

dp[0][0] = 1, dp[1][0] = 1, dp[0][1] = 1
dp[i][j] = dp[i-1][j] + dp[i][j-1]
因為要到達 (i, j)，機器人可能從上方 (i-1, j) 或左邊 (i, j-1) 來，所以要把他們的路徑數相加。
當把每個格子都計算完畢後，dp[n-1][m-1] 也就是到達最右下角那格的可能路徑數就是我們要的答案囉。

row dp (4*3)
0 1 2 3
0 1 1 1 1
1 1 1 1 1
2 1 1 1 1

i=1 j=1 -> dp[1][1] = dp[0][1] + dp[1][0] = 1 + 1 = 2
i=1 j=2 -> dp[1][2] = dp[0][2] + dp[1][1] = 1 + 2 = 3
i=1 j=3 -> dp[1][3] = dp[0][3] + dp[1][2] = 1 + 3 = 4
i=2 j=1 -> dp[2][1]
i=2 j=2 -> dp[2][2]
i=2 j=3 -> dp[2][3]
'''
def uniquePaths(m, n):
    # create m*n list.
    dp = [[1 for _ in range(m)] for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    print(dp)
    return dp[n-1][m-1]

print(uniquePaths(3,2)) # 3