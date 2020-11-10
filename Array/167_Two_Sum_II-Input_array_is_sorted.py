'''
Solution: Hash Map

i=0, num=2, diff=6-2=4, mapping={4:0+1}
i=1, num=3, diff=6-3=3, mapping={4:0+1, 3:1+1}
i=2, num=4, in mapping
'''
def twoSum(numbers, target):
    mapping = {}
    for i in range(len(numbers)):
        if numbers[i] in mapping:
            return [mapping[numbers[i]], i+1]
        else:
            diff = target - numbers[i]
            mapping[diff] = i + 1

print(twoSum([2,7,11,15], 9)) # [1,2]
print(twoSum([2,3,4], 6)) # [1,3]
print(twoSum([-1,0], -1)) # [1,2]