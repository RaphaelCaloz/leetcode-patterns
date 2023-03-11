# This template can be applied to problems
# that follow the
# "DFS from each unvisited node/Island" pattern

class Solution:
    def dfs(self, grid, visited, i, j):
        # For some problems, "visited" can be removed,
        # if grid[i][j] can be set to a special character
        # that indicates that node (i, j) has been visisted

        # Generally, one condition of the following line of code
        # is specific to the problem this template is being applied to.
        # As an example, here, we have grid[i][j] == '0', but this might
        # have to be modified depending on the problem.
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or visited[i][j] or grid[i][j] != 1:
            return
        
        visited[i][j] = True
        self.dfs(grid, visited, i+1, j)
        self.dfs(grid, visited, i, j+1)
        self.dfs(grid, visited, i-1, j)
        self.dfs(grid, visited, i, j-1)
    
    def numIslands(self, grid):
        if not grid:  # Optional depending on the problem's constraints
            return 0
        count = 0  # Problem specific
        # For some problems, "visited" is not required and is a waste of memory
        visited = [[False]*len(grid[0]) for _ in range(len(grid))]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not visited[i][j]:
                    self.dfs(grid, i, j)
                    count += 1  # problem specific (num of islands)
        return count
                
        
        

    