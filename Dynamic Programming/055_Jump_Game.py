'''
Solution: Dynamic programming

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, 
then 3 steps to the last index.

從後面往前看，若前一個index+本身的值 >= 最後一個index -> 更新最後一個index
Success Case:
[2,3,1,1,4]
i=3, nums[3]=1 + 3 >= 4 -> lastIndex=3
i=2, nums[2]=1 + 2 >= 3 -> lastIndex=2
i=1, nums[1]=3 + 1 >= 2 -> lastIndex=1
i=0, nums[0]=2 + 0 >= 1 -> lastIndex=0

Fail Case:
[3,2,1,0,4]
i=3, nums[3]=0 + 3 >= 4 -> No -> lastIndex=4
i=2, nums[2]=1 + 2 >= 4 -> No -> lastIndex=4
i=1, nums[1]=1 + 2 >= 4 -> No -> lastIndex=4
i=0, nums[0]=3 + 0 >= 4 -> No -> lastIndex=4
'''
def canJump(nums):
    lastIndex = len(nums) - 1
    for i in range(len(nums)-2, -1, -1): # 3,2,1,0
        if nums[i] + i >= lastIndex:
            lastIndex = i
    return lastIndex == 0

print(canJump([2,3,1,1,4])) # true