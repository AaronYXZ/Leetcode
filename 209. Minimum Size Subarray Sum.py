'''

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

click to show more practice.


'''

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        
        ## https://github.com/kamyu104/LeetCode/blob/master/Python/minimum-size-subarray-sum.py

        start= 0
        minSize = 2**32 -1
        sums = 0
        
        for end in range(len(nums)):
            sums += nums[end]
            while sums >= s:
                minSize = min(minSize, end - start +1)
                sums = sums - nums[start]
                start += 1
            
        return 0 if minSize == 2**32-1 else minSize
    