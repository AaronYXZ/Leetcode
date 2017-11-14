'''

Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ## http://blog.csdn.net/linhuanmars/article/details/20593391
        
        ## https://github.com/shichao-an/leetcode-python/blob/master/search_for_a_range/solution2.py
        
        n = len(nums)
        if n < 1:
            return [-1, -1]
        left = 0
        right = n - 1
        left_res = -1
        right_res = -1
        # Search for left bound (first occurence of target)
        while left + 1 < right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid
            else:
                right = mid
        if nums[left] == target:
            left_res = left
        elif nums[right] == target:
            left_res = right
        else:
            return [-1, -1]

        # Search for right bound (last occurence of target)
        left = 0
        right = n - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if target >= nums[mid]:
                left = mid
            else:
                right = mid
        if nums[right] == target:
            right_res = right
        elif nums[left] == target:
            right_res = left
        
        return [left_res, right_res]
                    
                
