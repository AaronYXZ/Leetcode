'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range.
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

'''


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        pos = 1
        res = 0
        
        if x < 0:
            pos = -1
            x = x* pos
        
        
        while x!= 0:
            res = res *10 + x%10
            if res > 2**31 -1:
                return 0
            x = x/10
        
        return res * pos
