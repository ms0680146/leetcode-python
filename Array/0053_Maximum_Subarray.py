'''
Solution: Array, Dynamic Programming
nums = [-2,1,-3,4,-1,2,1,-5,4]
local_sum = [-2,1,-2,4,3,5,6,1,5]
'''
def maxSubArray(nums):
    local_sum = []
    local_sum.insert(0, nums[0])

    for i in range(1, len(nums)): # 1,2,3..
        result = nums[i] + local_sum[i-1]
        if (nums[i] > result):
            local_sum.insert(i, nums[i])
        else:
            local_sum.insert(i, result)
    return max(local_sum)
    
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # [4,-1,2,1] has the largest sum = 6
print(maxSubArray([1])) # output=1
print(maxSubArray([0])) # output=0
print(maxSubArray([-1])) # output=-1

