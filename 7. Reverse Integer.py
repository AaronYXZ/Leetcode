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