class solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(). set()

        def dfs (r, c, visit, previous):
            if ( 
                (r,c) in visit or \
                r < 0 or 
                c < 0 or
                r == rows or 
                c == rows or
                heights[r][c] < previous
            ): return

            visit.add((r,c))
            directions =  [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc, visit, heights[r][c])

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols-1])


        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res