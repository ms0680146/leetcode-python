'''
Given an m x n board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, 
where "adjacent" cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

DFS 搜度搜尋演算法
找出接下來的四周圍是否包含 word

Input: board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
], word = "ABCCED"

Output: true
'''

def exist(board, word):
    for r in range(len(board)):
        for c in range(len(board[r])):
            if search(board, r, c, word, 0):
                return True
    return False


def search(board, row, col, word, wordIndx):
    if wordIndx == len(word):
        return True
    if row < 0 or col < 0 or row >= len(board) or col >= len(board[row]) or board[row][col] != word[wordIndx]:
        return False
    
    tmp = board[row][col]
    board[row][col] = None

    found = search(board, row - 1, col, word, wordIndx + 1) \
        or search(board, row + 1, col, word, wordIndx + 1) \
        or search(board, row, col - 1, word, wordIndx + 1) \
        or search(board, row, col + 1, word, wordIndx + 1) 
    
    board[row][col] = tmp
    
    return found