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
    if not grid or not grid[0]:
        return 0

    islands = 0
    visit = set()
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
      if ( 
          r not in range(rows)
          or c not in range(cols)
          or grid[r][c] == '0'
          or (r, c) in visit
      ): return

      visit.add((r,c))
      directions =  [[0, 1], [0, -1], [1, 0], [-1, 0]]
      for dr, dc in directions:
          dfs(r + dr, c + dc)

    for r in range(rows): # len=4 => 0,1,2,3
        for c in range(cols): # len=5=> 0,1,2,3,4
            if grid[r][c] == '1' and (r, c) not in visit:
                islands += 1
                dfs(grid, r, c)
    return islands

    
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(numIslands(grid))


## BFS
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def bfs(i, j):
            queue = deque([(i, j)])
            while queue:
                row, col = queue.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == '1':
                        grid[nr][nc] = '0'  # Mark as visited
                        queue.append((nr, nc))

        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    num_islands += 1
                    bfs(i, j)

        return num_islands

# Test cases
solution = Solution()
grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
print(solution.numIslands(grid1))  # Output: 1

grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(solution.numIslands(grid2))  # Output: 3
