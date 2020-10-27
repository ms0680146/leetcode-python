'''
Solution: Pointer

i=0, [1,1,1,2,2] -> [1,1,2,2]
i=0, [1,1,2,2] -> [1,2,2]
i=0, [1,2,2] -> i += 1
i=1, [1,2,2] -> [1,2]
'''
def removeDuplicates(nums):
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i+1]:
            del nums[i]
        else:
            i += 1
    return nums

print(removeDuplicates([1,1,2])) # output=2
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4])) # output=5