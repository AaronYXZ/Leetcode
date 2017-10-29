class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x1 = 0
        x2 = x
        while x!=0:
            x1 = x1 * 10 + x % 10
            x = x/10
        
        return x1 ==x2