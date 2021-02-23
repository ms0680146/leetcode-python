'''
Top Down Dynamic Programming

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12)

Base Case:
ways('') -> 1
ways('011') -> 0

Recursive Case:
ways('12345') -> 'a' + ways('2345') or 'l' + ways('345')
ways('27345') -> 'b' + ways('7345')

Test Case:
numDecodings('12')
memo = [0,0,0], helper('12', 2, memo)
first recursive: helper('12', 2, memo) -> helper('12', 1, memo) + helper('12', 0, memo)
second recursive: helper('12', 1, memo) -> helper('12', 0, memo)
third recursive: helper('12', 0, memo) -> 1
'''
def numDecodings(s):
    memo = [0 for i in range(len(s)+1)]
    return helper(s, len(s), memo)

def helper(s, len_s, memo):
    # Base case: numDecodings('') -> 1
    if len_s == 0:
        return 1
    # Base case: numDecodings('011') -> 0
    start = len(s) - len_s
    if s[start] == '0':
        return 0
    
    if memo[len_s] != 0:
        return memo[len_s]
    
    # helper('12345', k) = helper('12345', k-1) + helper('12345', k-2)
    # helper('27345', k) = helper('27345', k-1)
    result = helper(s, len_s - 1, memo)
    if len_s >= 2 and int(s[start:start+2]) <= 26: # 數字介於 10~26 之間才可以被decode
        result += helper(s, len_s - 2, memo)
        
    memo[len_s] = result
    return result 

'''
Button Up Dynamic Programming
i: 1234
s:'2112'
f(0) = 1
f(1) = 1
f(2) = f(0) + f(1) = 2
f(3) = f(1) + f(2) = 3
'''
def numDecodingsButtonUp(s):
    dp = [0 for _ in range(len(s) + 1)]
    dp[0] = 1
    if s[0] == '0':
        return 0
    else:
        dp[1] = 1
    
    for i in range(2, len(s) + 1): #'12' -> range(2, 3) -> 2
        if s[i-1] != '0':
            dp[i] = dp[i-1]
        
        if 10 <= int(s[i-2:i]) <= 26:
            dp[i] += dp[i-2]
    
    return dp[len(s)]