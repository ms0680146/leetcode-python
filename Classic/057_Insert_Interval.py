'''
Solution: Array

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

while loop intervals
check each interval and newInterval:
1. interval.end < newInterval.start -> 沒交集 -> store into result
2. interval.start > newInterval.end -> 沒交集 -> store into result
3. 其餘為有交集 -> 更新 newInterval -> store into result
'''
def insert(intervals, newInterval):
    result = []
    i = 0
    while i < len(intervals):
        if intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
        elif intervals[i][0] > newInterval[1]:
            result.append(intervals[i])
        else:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
        i += 1
    result.append(newInterval)
    result.sort(key=lambda x:x[0])

    return result

print(insert([[1,3],[6,9]], [2,5])) # [[1,5],[6,9]]