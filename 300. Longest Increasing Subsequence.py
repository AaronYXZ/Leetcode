'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
'''

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## http://bookshadow.com/weblog/2015/11/03/leetcode-longest-increasing-subsequence/

        size = len(nums)
        dp = [1] * size
        for x in range(size):
            for y in range(x):
                if nums[x] > nums[y]:
                    dp[x] = max(dp[x], dp[y]+1)
        return max(dp) if dp else 0

