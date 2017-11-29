''' 

Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]

Related problem: Reverse Words in a String II
'''

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        ## http://blog.csdn.net/ebowtang/article/details/50449688
        ## https://github.com/shichao-an/leetcode-python/blob/master/rotate_array/solution.py

        n = len(nums)
        k = k % n
        self.reverse(nums, 0, n - 1)  ## 1,2,3,4,5,6,7 --> 7 6 5 4 3 2 1
        self.reverse(nums, 0, k - 1)  ## 7 6 5 4 3 2 1 --> 5 6 7 4 3 2 1
        self.reverse(nums, k, n - 1)  ## 5 6 7 4 3 2 1 --> 5 6 7 1 2 3 4

    def reverse(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        
        