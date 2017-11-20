'''

Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.

'''

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        ## https://github.com/gavinfish/leetcode-share/blob/master/python/063%20Unique%20Paths%20II.py
        ## https://siddontang.gitbooks.io/leetcode-solution/content/dynamic_programming/unique_paths.html
        
        ## Pay attention to the first value obstacleGrid[0][0]
        if obstacleGrid[0][0] == 1:
            return 0
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]  
        dp[0][0] =1
        
        ## Pay attention to the case when m = 1 or n = 1
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] if obstacleGrid[i][0] == 0 else 0
        for j in range(1,n):
            dp[0][j] = dp[0][j-1] if obstacleGrid[0][j] == 0 else 0
            
        for i in range(m-1):
            for j in range(n-1):
                if obstacleGrid[i+1][j+1] == 1:
                    dp[i+1][j+1] = 0
                else:
                    dp[i+1][j+1] = dp[i][j+1]+dp[i+1][j]
        return dp[m-1][n-1]