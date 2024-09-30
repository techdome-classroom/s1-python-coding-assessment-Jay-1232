class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:

    # Edge case: if the grid is empty, return 0
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        visited = set()
        
        # Helper function for DFS
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 'W' or (r, c) in visited:
                return
            # Mark the current cell as visited
            visited.add((r, c))
            
            # Perform DFS on the 4 possible directions (up, down, left, right)
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left
        
        island_count = 0
        
        # Loop through every cell in the grid
        for r in range(rows):
            for c in range(cols):
                # Start a DFS if we find an unvisited land cell
                if grid[r][c] == 'L' and (r, c) not in visited:
                    dfs(r, c)
                    island_count += 1
        
        return island_count          
    
