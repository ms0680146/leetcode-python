'''
Given an array of integers nums and an integer k, 
return the total number of continuous subarrays whose sum equals to k.

EX:
Input: nums = [1,2,3], k = 3
Output: 2

Brute force: List all subarrays.
nums = [1,2,3]
subarray = [[1], [1,2], [1,2,3], [2], [2,3], [3]]
i=0 j=1 subarray=[0:1]=[1]
i=0 j=2 subarray=[0:2]=[1,2]
i=0 j=3 subarray=[0:3]=[1,2,3]
i=1 j=2 subarray=[1:2]=[2]
i=1 j=3 subarray=[1:3]=[2,3]
i=2 j=3 subarray=[2:3]=[3]
'''

def subarraySum(nums, k):
    result = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)+1):
            subarray = nums[i:j]
            result.append(subarray)
    
    count = 0
    for i in range(len(result)):
        sum_subarray = sum(result[i])
        if sum_subarray == k:
            count+=1
    return count

'''
Hash Map
subarray sum = sum(0, x) - sum(0, y)
[1,5,7,9,11] 7,9 k=15 
[1,5,7,9] 
[1,5]
'''
def subarrayHashMap(nums, k):
    hash_map = {0:1}
    total = 0
    count = 0

    for i in range(len(nums)):
        total += nums[i]
        if total - k in hash_map:
            count += hash_map[total-k]
        
        if total in hash_map:
            hash_map[total] += 1
        else:
            hash_map[total] = 1
    return count

