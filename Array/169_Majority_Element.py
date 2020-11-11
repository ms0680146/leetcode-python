'''

'''
def majorityElement(nums):
    count_dict = {}
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    for value, count in count_dict.items():
        if count > len(nums) / 2:
            return value
    return -1

print(majorityElement([3,2,3]) # 3
print(majorityElement([2,2,1,1,1,2,2]) # 2