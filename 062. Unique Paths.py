'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

'''

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        ## https://github.com/gavinfish/leetcode-share/blob/master/python/062%20Unique%20Paths.py
        ## https://siddontang.gitbooks.io/leetcode-solution/content/dynamic_programming/unique_paths.html
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(m-1):
            for j in range(n-1):
                dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j]
            
        return dp[m-1][n-1]
