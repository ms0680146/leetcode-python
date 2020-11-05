'''
Solution: Array

rowIndex: 5
output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

def getRow(rowIndex):
    result = []
    for row in range(rowIndex+1): #0,1,2,3
        result.append([])
        for column in range(row+1):
            if column in (0,row):
                result[row].append(1)
            else:
                result[row].append(result[row-1][column-1] + result[row-1][column])
    return result[rowIndex]

print(getRow(3)) # [1,3,3,1]
print(getRow(0)) # [1]
print(getRow(1)) # [1,1]
