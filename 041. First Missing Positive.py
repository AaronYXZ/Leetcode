'''

Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.



'''

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## http://www.cnblogs.com/AnnieKim/archive/2013/04/21/3034631.html
        ## https://github.com/gavinfish/leetcode-share/blob/master/python/041%20First%20Missing%20Positive.py  
        i = 0
        length = len(nums)
        
        while i < length:
            current = nums[i]
            if current <= 0 or current > length or nums[current - 1] == current:
                i += 1
            else:
                nums[current - 1], nums[i] = nums[i], nums[current - 1]

        for i in range(length):
            if nums[i] != i + 1:
                return i + 1
        return length + 1
