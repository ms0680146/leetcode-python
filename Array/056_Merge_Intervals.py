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
    intervals.sort(key=lambda pair: pair[0])
    output = [intervals[0]]

    for start, end in intervals[1:]:
        lastEnd = output[-1][1]

        if start <= lastEnd:
            # 若新進來的區間頭 <= 原本的區間尾, merge
            output[-1][1] = max(lastEnd, end)
        else:
            output.append([start, end])
    return output

print(merge([[1,3],[2,6],[8,10],[15,18]])) # [[1,6],[8,10],[15,18]]