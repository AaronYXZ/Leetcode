'''

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

'''


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        ## 利用两个指针从数组的两侧开始向中间移动，寻找第一对和为target的两个数即为所求。
        l , r = 0, len(numbers)-1
        while l < r:
            total = numbers[l] + numbers[r]
            if  total== target:
                return l+1, r+1
            elif total < target:
                l +=1
            else:
                r -=1
            
                    
            