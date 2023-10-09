'''
Solution: Array
nums=[1,3,5,6], target=5
output=2
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

'''
Binary search
'''
def searchInsertBS(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left += 1
        else:
            right -= 1
    return left