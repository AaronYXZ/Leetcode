class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        n = len(nums)
        if n <2:
            return n
        j = 0
        for i in range(1, n):
            if nums[j] != nums[i]:
                nums[j+1] = nums[i]
                j +=1
        return j+1