'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
'''


## http://blog.csdn.net/linhuanmars/article/details/21354751
## https://github.com/gavinfish/leetcode-share/blob/master/python/055%20Jump%20Game.py

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        index = 0
        longest = nums[index]
        length = len(nums)
        
        if length ==1:
            return True
        
        while index <= longest:
            if longest >= length -1:
                return True
            longest = max(longest, index + nums[index])
            index +=1 
            
        return False
