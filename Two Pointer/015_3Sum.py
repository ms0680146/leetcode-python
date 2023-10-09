'''
Solution: Two Pointers Collide

1. Sort nums.
2. Foor loop nums and fix i index.
3. put left, right index collide to find closet target.
  i-->  
[-4, -1, -1, 0, 1, 2]
      l-->      <--r
https://www.youtube.com/watch?v=jzZsG8n2R9A
'''
def threeSum(nums):
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n):
        l = i + 1
        r = n - 1

        if i > 0 and nums[i] == nums[i-1]: # skip duplicate (-4, -1, -1..)
            continue
        
        # two sum II
        while l < r:
            three_sum = nums[i] + nums[l] + nums[r]
            if three_sum > 0:
                r -= 1
            elif three_sum < 0:
                l += 1
            else:
                result.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:  # skip duplicate (-1, -1..)
                    l += 1
                while l < r and  nums[r] == nums[r+1]:  # skip duplicate
                    r -= 1
    return result


print(threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
