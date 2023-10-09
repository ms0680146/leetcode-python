'''
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
------------------------------------------------------------------
觀察 brute force 的規則：
2
23
231
2312 --> greater than or equal 7 --> 計算 subarray_len
23124 --> 不用計算
231243 --> 不用計算

3
31
312
3124 --> greater than or equal 7
31243 --> 不用計算

1
12
124 --> greater than or equal 7
1243 --> 不用計算

2
24
243 --> greater than or equal 7

4
43 --> greater than or equal 7

---------------------------------------------------------
一開始 windowStart 指向 2, 然後 windowEnd 會慢慢擴張
當擴張到 [2,3,1,2] 這個情況時，因為 sum 已經 >= 7
所以 windowStart 會開始右移
也就是說，原本暴力法會考慮的 [2,3,1,2,4] 跟 [2,3,1,2,4,3] 就不會被考慮到
'''
def minSubArrayLen(target, nums):
    start = 0
    window_sum = 0
    global_len_of_subarray = float('inf')
    local_len_of_subarray = 0
    
    for i in range(len(nums)):
        window_sum += nums[i]
        while window_sum >= target:
            local_len_of_subarray = i - start + 1
            global_len_of_subarray = min(local_len_of_subarray, global_len_of_subarray)
            window_sum -= nums[start]
            start += 1
    return global_len_of_subarray if global_len_of_subarray != float('inf') else 0