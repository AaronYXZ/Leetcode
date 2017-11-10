'''
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. 
If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
You are responsible to gather all the input requirements up front.
'''



class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        str = str.strip()
        if not str:
            return 0
        MAX_INT = 2**31-1
        MIN_INT = -2**31
        
        ret = 0
        overflow = False
        pos = 0
        sign = 1
        
        if str[pos] == '-':
            pos+=1
            sign = -1
        elif str[pos] == '+':
            pos+=1
            
        for i in range(pos, len(str)):
            if not str[i].isdigit():
                break
            ret = ret * 10 + int(str[i])
            if not MIN_INT <= sign*ret <= MAX_INT:
                overflow = True
                break
        
        if overflow:
            return MAX_INT if sign == 1 else MIN_INT
        else:
            return sign * ret
        
