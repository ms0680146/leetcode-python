'''
Solution: Array
'''
def generate(numRows):
    result = []
    for i in range(numRows): # rows -> 0,1,2,3,4
        result.append([])
        for j in range(i+1):  # columns 
            if j in (0,i): # 第一個和最後一個都是1
                result[i].append(1)
            else: # 中間的是由上面那層的前兩個相加
                result[i].append(result[i-1][j-1] + result[i-1][j])
    return result

print(generate(5))

'''
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

