'''
DFS(深度搜尋演算法)
An island is surrounded by water 
and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Ex1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
----
Ex2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
---

Solution:
origin
["1","1","0","0","0"],
["1","1","0","0","0"],
["0","0","1","0","0"],
["0","0","0","1","1"]

["0","0","0","0","0"],
["0","0","0","0","0"],
["0","0","1","0","0"],
["0","0","0","1","1"]

island = 0
0,0 -> '1' -> '0' -> top x, bottom, left x, right 0
1,0 -> '1' -> '0' -> top 0, bottom 0, left x, right
1,1 -> '1' -> '0' -> top, bottom 0m left 0, right 0
0,1 -> '1' -> '0' -> top x, bottom 0, left 0, right 0

'''

def numIslands(grid):
    islands = 0
    for r in range(len(grid)): # len=4 => 0,1,2,3
        for c in range(len(grid[r])): # len=5=> 0,1,2,3,4
            if grid[r][c] == '1':
                findSurrounds(grid, r, c)
                islands += 1
    return islands

def findSurrounds(grid, r, c):
    grid[r][c] = '0'
    surrounds = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)] # top, bottom, left, right
    
    for row, col in surrounds:
        if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[row]) and grid[row][col] == '1':
            findSurrounds(grid, row, col)
    
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(numIslands(grid))
