'''

Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ## http://fisherlei.blogspot.com/2015/10/leetcode-product-of-array-except-self.html
        '''
        另一种解法，可以分成三种情况：
        数组中有一个以上的0出现， 比如 [1,2, 0, 0, 3, 4]， 最后的结果肯定都是0： [0,0,0,0,0,0]
        数组中有一个0出现，比如[1,2,0,3,4]，按照题目的定义，最后的输出结果是[0,0,24,0,0]. 除了0的那一位是有值，其他位都是0
        数组中没有0， 假设数组位[a0, a1, a2, ......], 其中所有数值的乘积为M， 那个数组的输出就是[M/a0, M/a1, M/a2.....].
        '''
        countZero = 0
        for item in nums:
            if item == 0:
                countZero +=1
        
        if countZero > 1:
            return [0 for _ in nums]
        elif countZero  == 1:
            totalZero = 1
            for item in nums:
                if item!=0:
                    totalZero *= item
            return [0 if item!=0 else totalZero for item in nums]
        else:
            total = 1
            for item in nums:
                total*=item
            return [total / item for item in nums]