'''
Solution: Two Pointers(反向)
[1,8,6,2,5,4,8,3,7] -> len = 9
判斷 left 和 right 哪邊比較高，留下比較高的，另一個往中間縮
'''
def maxArea(nums):
    local_area = 0
    global_area = 0
    left = 0
    right = len(nums) - 1

    while left < right:
        button = right - left
        height = min(nums[left], nums[right])
        local_area = button * height
        global_area = max(local_area, global_area)

        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1

    return global_area

print(maxArea([1,1])) # 1
print(maxArea([4,3,2,1,4])) # 16
print(maxArea([1,2,1])) # 2


'''
brute force
'''
def maxAreaBruteForce(nums):
    res = 0
    for l in range(len(nums)):
        for r in range(l+1, len(nums)):
            button = r - l
            height = min(nums[l], nums[r])
            area = button * height
            res = max(area, res)
    return res