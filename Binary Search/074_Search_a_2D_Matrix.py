'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        button = rows - 1
        while top <= button:
            mid_row = (top + button) // 2
            if matrix[mid_row][0] > target:
                button = mid_row - 1
            elif matrix[mid_row][0] < target:
                top = mid_row + 1
            else:
                break
        possible_row = (top + button) // 2
        left = 0
        right = cols - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[possible_row][mid] > target:
                right = mid - 1
            elif matrix[possible_row][mid] < target:
                left = mid + 1
            else:
                return True
        return False