'''
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

'''

def topKFrequent(nums: List[int], k: int) -> List[int]:
    numCountMap = {} # {1: 3, 2: 2, 3: 1}
    for num in nums:
        if num in numCountMap:
            numCountMap[num] = numCountMap.get(num) + 1
        else:
            numCountMap[num] = 1

    # sorted(numCountMap.values(),reverse=True) = [3,2,1]
    topKCount = sorted(numCountMap.values(),reverse=True)[k-1]
    res = []
    for num in numCountMap:
        if numCountMap[num] >= topKCount:
            res.append(num)
    return res