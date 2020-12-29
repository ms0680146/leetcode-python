'''
Solution: Array

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

1. 必須依照 intervals[i][0] 大小排序 intervals 
2. 開一個新的 result 存每個區間
3. 若原本的區間尾 > 新進來的區間頭 -> 代表 Overlapping，更新原本的區間
'''
def merge(intervals):
    result = []
    intervals.sort(key=lambda x:x[0])

    # intervals 沒有半個子區間或是只有一個子區間 -> 直接回傳 intervals
    if len(intervals) == 0 or len(intervals) == 1:
        return intervals
    # intervals 至少有兩個子區間
    result.append(intervals[0])
    for i in range(1, len(intervals)): #1,2,3
        pre_end = result[-1][1]
        cur_start = intervals[i][0]
        cur_end = intervals[i][1]
        if pre_end >= cur_start:
            result[-1][1] = max(pre_end, cur_end)
        else:
            result.append(intervals[i])

    return result

print(canJump([2,3,1,1,4])) # true