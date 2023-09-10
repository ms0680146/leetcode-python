'''
Solution: Matrix
rotate the image in-place

solution1: 
ex: 4x4 matrix
  l        r
t 1  2  3  4
  5  6  7  8
  9  10 11 12
b 13 14 15 16

https://www.youtube.com/watch?v=fMSJSS7eO1w
----------

'''
def rotate(matrix):
    l, r = 0, len(matrix) - 1
    while l < r:
        for i in range(r - l):
            top, bottom = l, r

            # save the topleft
            topLeft = matrix[top][l + i]

            # move bottom left into top left
            matrix[top][l + i] = matrix[bottom - i][l]

            # move bottom right into bottom left
            matrix[bottom - i][l] = matrix[bottom][r - i]

            # move top right into bottom right
            matrix[bottom][r - i] = matrix[top + i][r]

            # move top left into top right
            matrix[top + i][r] = topLeft
        r -= 1
        l += 1


print(rotate([[1,2,3],[4,5,6],[7,8,9]])) # [[7,4,1],[8,5,2],[9,6,3]]