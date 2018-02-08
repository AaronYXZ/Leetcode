'''

Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.

'''

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        ## Practice DP in O(n**2), but could in O(n) or even O(1)!
        
        ## https://www.hrwhisper.me/leetcode-integer-break/
        ## http://bookshadow.com/weblog/2016/04/19/leetcode-integer-break/
        dp = [1]* (n+1)
        for i in xrange(1, n+1):
            for j in xrange(1, i+1):
                if i+j <=n:
                    dp[i+j] = max(max(dp[i], i) * max(dp[j], j), dp[i+j]) 
        return dp[n]