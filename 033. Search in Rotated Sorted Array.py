'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        ## http://blog.csdn.net/linhuanmars/article/details/20525681
        ## http://fisherlei.blogspot.com/2013/01/leetcode-search-in-rotated-sorted-array.html
        
        
        ## https://github.com/gavinfish/leetcode-share/blob/master/python/033%20Search%20in%20Rotated%20Sorted%20Array.py
        l , r = 0, len(nums)-1
        
        while l <= r:
            mid = (l+r) // 2
            if target == nums[mid]:
                return mid
            
            if nums[mid] >= nums[l]:
                if (nums[l] <= target) and (target <= nums[mid]):
                    r = mid-1
                else:
                    l = mid+1
            elif nums[mid] < nums[l]:
                if (nums[mid] <= target) and (target <= nums[r]):
                    l = mid + 1
                else:
                    r = mid - 1
    
        return -1  
