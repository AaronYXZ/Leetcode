class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        step = numRows * 2 - 2
        # first row
        ret = s[::step]
        
        # middle rows
        for i in range(1, numRows - 1):
            for j in range(i, len(s), step):
                ret += s[j]
                if j + (step - i * 2) < len(s):
                    ret += s[j + (step - i * 2)]
        # last row
        ret += s[numRows - 1::step]
        return ret