'''
Array
Given an m x n matrix. 
If an element is 0, set its entire row and column to 0. Do it in-place.

Ex:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
'''

def setZeroes(matrix):
    row_record = []
    col_record = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                row_record.append(row)
                col_record.append(col)
    
    for i in row_record:
        for j in col_record:
            setEntireRowToZero(i, matrix)
            setEntireColToZero(j, matrix)

def setEntireRowToZero(row, matrix):
    for i in range(len(matrix[row])):
        matrix[row][i] = 0

def setEntireColToZero(col, matrix):
    for j in range(len(matrix)):
        matrix[j][col] = 0