'''
Problem:
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

'''
Dynamic Programming
Top Down DFS
- Base Case
- 利用父問題傳下來的值做計算
- 把值傳給子問題做 recursion
'''
class Solution:
    sum_count = 0
    # top down dp.
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 1
        self.dfs(1, s, len(s))
        return self.sum_count
    
    def dfs(self, count, s, len_s):
        # Base Case
        if len_s == 0:
            self.sum_count += count
            return
        # 利用父問題傳下來的值做一些計算 (這邊要到最後一層在做計算)
        # Edge case: numDecodings('011') -> 0
        start = len(s) - len_s
        if s[start] == '0':
            return 0
        # 把值傳給子問題繼續計算
        self.dfs(count, s, len_s - 1)
        if len_s >= 2 and int(s[start:start+2]) <= 26:
            self.dfs(count, s, len_s - 2)
        

'''
Dynamic Programming
Button Up DFS
- Base Case
- 向子問題要答案(return value)
- 利用子問題的答案構建當前問題的答案
- 返回答案給父問題
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