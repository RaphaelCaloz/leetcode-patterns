class Solution:
    # Returns the prefix sum of the input matrix, where return_matrix[r+1][c+1] = sum of all matrix[i][j], where i <= r, j <= c
    # The first column and row is padded with zeros.
    def prefix_sum(self, matrix):
        self.dp = [[0]*( len(matrix[0])+1 ) for _ in range( len(matrix)+1 )]
            
        # calculate prefix sum
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.dp[r+1][c+1] = matrix[r][c] + self.dp[r+1][c] + self.dp[r][c+1] - self.dp[r][c]
        return self.dp


sol = Solution()
mat = [[1,5,9],[10,11,13],[12,13,15]]

# prefix_sum usage
print("[")
for row in sol.prefix_sum(mat):
    print(row)
print("]")