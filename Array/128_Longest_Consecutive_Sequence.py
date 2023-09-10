'''
Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''

def longestConsecutive(nums: List[int]) -> int:
    longest = 0
    numsSet = set(nums)
    for num in nums:
        if (num-1) not in numsSet:
            length=1
            while (num + length) in numsSet:
                length += 1
            longest = max(length, longest)
    return longest



# [100, 4, 200, 1, 3, 2]
# use set() to store these numbers
# 100-1=99, not in set, it is the start of sequence: 100 ->
# 100+1=101, not in set, we can not add number after 100

# 4-1=3, in set, it is not the start of sequence

# 200-1=100, not in set, it is the start of sequence: 200 ->
# 200+1=201, not in set, we can not add sequence after 200 

# 1-1=0, not in set, it is the start of sequence: 1 ->
# 1+1=2, in set, we can add number after 1, 1 -> 2
# 2+1=3, in set, we can add number after 2, 1 -> 2 -> 3
# 3+1=4,  in set, we can add number after 3, 1 -> 2 -> 3 -> 4
# 4+1=5, not in set, we can not add sequence after 4

# 3-1=2, in set, it is not the start of sequence

# 2-1=1, in set, it is not the start of sequence

