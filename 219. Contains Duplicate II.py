'''

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.



'''

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        ## http://www.jianshu.com/p/f4db6510d4f3
        d = {}
        for i, val in enumerate(nums):
            if nums[i] in d:
                j = d[val]
                if i - j <= k:
                    return True
            d[val] = i
        return False