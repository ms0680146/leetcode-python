'''
Solution: Hash Map

[2,7,11,15]
i=0, num=2 -> diff=9-2=7 -> mapping={2:0}
i=1, num=7 -> diff=9-7=2 -> yes, in mapping
'''
def twoSum(nums, target):
    mapping = {}
    for i in range(len(nums)): # 0,1,2,3
        diff = target - nums[i]
        if diff in mapping:
            return [mapping[diff], i]
        mapping[nums[i]] = i
    return False

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))