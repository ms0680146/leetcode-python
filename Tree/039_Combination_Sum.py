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
'''
class Solution:
    def combinationSum(self, candidates, target):
        self.result = []
        self.candidates = candidates
        self.dfs([], target, 0)
        return self.result

    def dfs(self, path, target, index):
        if target < 0:
            return
        if target == 0:
            self.result.append(path)
            return
        for i in range(index, len(self.candidates)):
            remain_target = target - self.candidates[i]
            self.dfs(path + [self.candidates[i]], remain_target, i)