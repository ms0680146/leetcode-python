'''
Solution: Matrix
rotate the image in-place

solution1: 
ex: 4x4 matrix
1  2  3  4
5  6  7  8
9  10 11 12
13 14 15 16

first round, i=0, j=0, outer loop
1(0,0)->top, 13(3,0)->1, 16(3,3)->13, 4(0,3)->16, top->4
second round, i=0, j=1, outer loop
2(0,1)->top, 9(2,0)->2, 15(3,2)->9, 8(1,3)->15, top->8
third round, i=0, j=2, outer loop (boundary)
3(0,2)->top, 5(1,0)->3, 14(3,1)->5, 12(2,3)->14, top->12
forth round, i=1, j=1, inner loop
6(1,1)->top, 10(2,1)->6, 11(2,2)->10, 7(1,2)->11, top->7
----------

'''
def rotate(matrix):
    n = len(matrix)
    for i in range(n//2):
        for j in range(i, n-i-1):
            # top = matrix[i][j]
            # left = matrix[n-j-1][i] # 13,9,5
            # right = matrix[j][n-i-1] # 4,8,12
            # button = matrix[n-i-1][n-j-1] # 16,15,14
            tmp = matrix[i][j]
            matrix[i][j] = matrix[n-j-1][i]
            matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
            matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
            matrix[j][n-i-1] = tmp


print(rotate([[1,2,3],[4,5,6],[7,8,9]])) # [[7,4,1],[8,5,2],[9,6,3]]