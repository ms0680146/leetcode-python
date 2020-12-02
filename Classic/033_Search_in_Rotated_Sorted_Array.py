'''
Solution: Binary Search

ex: [4,5,6,7,8,0,1,2,3] -> mid = 8, target = 5
分為左半及右半, 必定有一半是排序過的
4 < 8 -> 表示左半一定為排序過的, 檢查 target 是否在 4 ~ 8之間, 若存在則在左半繼續做BS

ex: [7,8,0,1,2,3,4,5,6] -> mid = 2, target = 5
分為左半及右半, 右半為排序過的, 檢查 target 是否在 2 ~ 6之間, 若存在則右半繼續做BS
'''
def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        
        # 左半已經排序過了
        if nums[left] <= nums[mid]:
            if target >= nums[left] and target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if target <= nums[right] and target >= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

print(search([4,5,6,7,0,1,2], 0)) # 4
print(search([4,5,6,7,0,1,2], 3)) # -1
print(search([1], 0)) # -1