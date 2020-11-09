'''
Solution: Array
'''
def searchInsert(nums, target):
    for i in range(len(nums)): #0,1,2,3
        if target == nums[i]:
            return i
        elif target < nums[i]:
            return i
    return i + 1
    
print(searchInsert([1,3,5,6], 5)) # output=2
print(searchInsert([1,3,5,6], 2)) # output=1
print(searchInsert([1,3,5,6], 7)) # output=4
print(searchInsert([1,3,5,6], 0)) # output=0
print(searchInsert([1], 0)) # output=0