class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dictMap = {}
        for index, value in enumerate(nums):
            if target - value in dictMap:
                return dictMap[target-value] , index 
            dictMap[value] = index