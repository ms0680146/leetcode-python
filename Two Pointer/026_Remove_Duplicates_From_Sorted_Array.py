'''
Pointer

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


'''
Two Pointer(同向)
Pseudo Code
1. initialize two pointer: i = 0, j = 0 
2. while j < len(arr):
     if need arr[j]:
       then we assign arr[i] = arr[j], i++, j++
     else: 
       j++

nums = [1,2,2,2,3,5,5] 
'''
def removeDuplicatesTwoPointer(nums):
    i = 0
    j = 0

    while j < len(nums):
        if i == 0 or nums[j] != nums[i-1]:
            nums[i] = nums[j]
            i += 1
            j += 1
        else:
            j += 1
    return i
