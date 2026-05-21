class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Edge case: If the grid is empty, return 0 islands
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])  # Get grid dimensions
        directions = [[1, 0],[-1, 0], [0, 1], [0, -1]]  # Down, Up, Right, Left
        islands = 0  # Counter for number of islands

        def dfs(r, c):
            # Base case: if out of bounds or at water, stop recursion
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            grid[r][c] = "0"  # Mark the cell as visited (sink the land)
            # Visit all 4 neighbors (DFS traversal)
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Traverse every cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If cell is land and not visited yet
                if grid[r][c] == "1":
                    dfs(r, c)      # Visit all connected land
                    islands += 1   # After DFS, we've found a full island

        return islands  # Return total number of islands

# 1. Loop over every cell in the grid.
# 2. If a cell is "1" (land), do DFS to mark all connected land cells as visited.
# 3. For each DFS call that starts on unvisited land, increment the island count.
# 4. After checking all cells, return the total island count.

# Time Complexity: O(m * n) - Each cell is visited once.
# Space Complexity: O(m * n) - Worst-case recursion stack (all land).


