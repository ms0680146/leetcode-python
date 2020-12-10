'''
Solution: DFS(深度搜尋演算法)

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