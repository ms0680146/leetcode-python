'''
Solution: Hash Map

numbers=[2,3,4], target=6
i=0, num=2, diff=6-2=4, mapping={2:0+1}
i=1, num=3, diff=6-3=3, mapping={2:0+1, 3:1+1}
i=2, num=4, diff=6-4=2, in mapping
'''
def twoSum(numbers, target):
    mapping = {}
    for i in range(len(numbers)):
        diff = target - numbers[i]
        if diff in mapping:
            return [mapping[diff], i+1]
        mapping[numbers[i]] = i + 1

print(twoSum([2,3,4], 6)) # [1,3]
print(twoSum([2,7,11,15], 9)) # [1,2]
print(twoSum([-1,0], -1)) # [1,2]


def twoSumTwoPointer(numbers, target):
    l, r = 0, len(numbers) - 1
    while l < r:
        curSum = numbers[l] + numbers[r]
        if curSum > target:
            r -= 1
        elif curSum < target:
            l += 1
        else:
            return [l+1, r+1]
    return -1


print(twoSum([2,3,4], 6)) # [1,3]
print(twoSum([2,7,11,15], 9)) # [1,2]
print(twoSum([-1,0], -1)) # [1,2]