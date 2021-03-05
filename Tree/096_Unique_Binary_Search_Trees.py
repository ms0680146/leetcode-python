'''
Solution: Tree, Dynamic Programming
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Input: numTrees(0), Output: 1
Input: numTrees(1), Output: 1
Input: numTrees(2) (use 1,2 as root), Output: numTrees(0)*numTrees(1) + numTrees(1)*numTrees(0)=2
Input: numTrees(3) (use 1,2,3 as root), Output: numTrees(0)*numTrees(2) + numTrees(1)*numTrees(1) + numTrees(2)*numTrees(0)

Button Up DFS
- Base Case
- 向子問題要答案(return value)
- 利用子問題的答案構建當前問題的答案
- 返回答案給父問題

O(n**2)
'''

class Solution:
    def numTrees(self, n):
        self.memo = [None for _ in range(n+1)]
        return self.dfs(n)
    
    def dfs(self, n):
        if n <= 1:
            return 1
        
        if self.memo[n] != None:
            return self.memo[n]
        
        result = 0
        for i in range(1, n+1): #1,2,3
            left = self.dfs(i-1)
            right = self.dfs(n-i)
            result += left * right
        
        self.memo[n] = result
        
        return result

