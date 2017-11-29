'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) / 2
            if nums[mid] <= nums[high]: #min位于左侧上升沿
                high = mid
            else: #min位于左侧上升沿与右侧上升沿之间
                low = mid + 1
        return nums[low]
        
        '''
        
        
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) / 2
            if nums[mid] <= nums[high]: #min位于左侧上升沿
                high = mid
            else: #min位于左侧上升沿与右侧上升沿之间
                low = mid + 1
        return nums[low]