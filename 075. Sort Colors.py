'''

Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

'''

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
  
        ## http://fisherlei.blogspot.com/2013/01/leetcode-sort-colors.html
        ## https://github.com/gavinfish/leetcode-share/blob/master/python/075%20Sort%20Colors.py
        l = m = 0
        r = len(nums)-1
        while m <= r:
            if nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                l+=1
                m+=1
            elif nums[m] == 1:
                m+=1
            else:
                nums[r], nums[m] = nums[m],nums[r]
                r-=1
            
            
