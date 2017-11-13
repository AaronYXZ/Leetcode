'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapper = {"I":1, 'V':5, 'X':10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        total = 0
        prev = 0
        for item in s:
            curr = mapper[item]
            total += curr
            if prev < curr:
                total = total - 2*prev
            prev = curr
            
        return total
