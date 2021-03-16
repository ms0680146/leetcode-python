'''
Solution:
因為前面的 currentSum 加上 num[i]，
如果不會讓 currentSum 變得比 num[i] 更大，
那就不如不要前面那些總計了，直接把 currentSum 改成 num[i] 繼續加總，
而在 currentSum 每次加總完也都和當前的 maxSum 比較一下，
如果比較大的話就更新 maxSum。

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
----------

'''
def maxSubArray(nums):
    max_sum, local_sum = nums[0], nums[0]
    for i in range(1, len(nums)): # 1,2,..
        local_sum += nums[i]
        if local_sum < nums[i]:
            local_sum = nums[i]
        
        if local_sum > max_sum:
            max_sum = local_sum
    
    return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6

'''
Brute Force Solution
列出所有的可能subarray，比較其 sum 值大小。
'''

def maxSubArrayBruteForce(nums):
    global_sum = float('-inf')
    for i in range(len(nums)):
        for j in range(i+1, len(nums)+1):
            local_sum = sum(nums[i:j])
            global_sum = max(global_sum, local_sum)
    return global_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6
    