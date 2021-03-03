'''
Solution1: Hash Map
'''
def containsDuplicate(nums):
    duplicate_dict = {}
    for num in nums:
        if num in duplicate_dict:
            duplicate_dict[num] += 1
        else:
            duplicate_dict[num] = 1

    for num, count in duplicate_dict.items():
        if count > 1:
            return True

    return False

'''
Solution2: Sort Array
'''
def containsDuplicate(nums):
    nums.sort()
    for i in range(len(nums)):
        if i < len(nums) -1 and nums[i] == nums[i+1]:
            return True
    return False

print(containsDuplicate([1,2,3,1])) # true
print(containsDuplicate([1,2,3,4])) # false
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2])) # true



