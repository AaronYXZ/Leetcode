'''

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.



'''


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        cont = 1
        j = 0
        i = 1
        l = len(nums)
        
        if l < 3:
            return l
        while i < l:
            if nums[j] != nums[i]:
                nums[j+1] = nums[i]
                j += 1
                i += 1
                cont = 1
            elif cont:
                nums[j+1] = nums[i]
                i +=1
                j +=1
                cont = 0
            else:
                i += 1 
        return j+1
                
                
