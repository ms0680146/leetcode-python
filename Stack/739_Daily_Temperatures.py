'''
Given an array of integers temperatures represents the daily temperatures
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]

'''

# brute force
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                print(i, j)
                if temperatures[j] > temperatures[i]:
                    res.append(j-i)
                    break
                elif j == len(temperatures) - 1:
                    res.append(0)
            if i == len(temperatures) - 1:
                res.append(0)
        return res
# stack
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # (tmp, index)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTmp, stackIndex = stack.pop()
                res[stackIndex] = i - stackIndex
            stack.append((t, i))
        return res