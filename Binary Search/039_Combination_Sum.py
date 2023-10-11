'''
Solution: Top Down DFS(深度搜尋演算法)
1. 把值透過參數的形式往下傳遞
2. top down dfs 一般來說不返回值
3. Pseudo Code:
- Base Case
- 利用父問題傳下來的值做計算
- 把值傳給子問題做 recursion

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
https://www.youtube.com/watch?v=GBKI9VSKdGg&t=854s
'''
class Solution:
    def combinationSum(self, candidates, target):
        res = []
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i+1, cur, total)
        dfs(0, [], 0)
        return res