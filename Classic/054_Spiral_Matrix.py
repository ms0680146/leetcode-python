'''
Solution: Multi Array

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

row -> 橫的 / column -> 直的
Go right -> Go down -> Go left -> Go up -> Go right -> ...
traverse right and increment rowBegin
traverse down and decrement colEnd
traverse left and decrement rowEnd
traverse up and increment colBegin
'''
def spiralOrder(matrix):
    result = []
    row_start = 0
    col_start = 0
    row_end = len(matrix) - 1
    col_end = len(matrix[0]) - 1
    direct = 0
    
    while len(result) != len(matrix) * len(matrix[0]): # 總元素必須相等
        if direct == 0: # Go right
            for i in range(col_start, col_end):
                result.append(matrix[row_start][i])
            row_start += 1
        if direct == 1: # Go down
            for i in range(row_start, row_end):
                result.append(matrix[i][col_end])
            col_end -= 1
        if direct == 2: # Go left
            for i in range(col_end, col_start-1, -1):
                result.append(matrix[row_end][i])
            row_end -= 1
        if direct == 3: # Go up
            for i in range(row_end, row_start-1, -1):
                result.append(matrix[i][col_start])
            col_start += 1

        direct = (direct + 1) % 4

    return result

print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]])) # [1,2,3,6,9,8,7,4,5]