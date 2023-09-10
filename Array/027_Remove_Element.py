'''
Solution: Pointer
- input: [3,2,2,3]
- removed element: 3

pointer=0, [3,2,2,3], remove nums[0],  [2,2,3]
pointer=0, [2,2,3], not remove, pointer+=1
pointer=1, [2,2,3], not remove, pointer+=1
pointer=2, [2,2,3], remove nums[2], [2,2]
'''
def removeElement(nums, val):
    pointer = 0
    while pointer <= len(nums) - 1:
        if nums[pointer] == val:
            del nums[pointer]
        else:
            pointer += 1
    return len(nums)

print(removeElement([3,2,2,3], 3)) # output=2, nums=[2,2]
print(removeElement([0,1,2,2,3,0,4,2], 2)) # output=5, nums=[0,1,4,0,3]