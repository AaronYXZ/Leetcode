'''
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

'''

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        ## https://siddontang.gitbooks.io/leetcode-solution/content/array/pascals_triangle.html
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        
        row = [1,1]
        for i in range(2, rowIndex+1):
            row.append(1)
            for j in range(i-1, 0, -1):
                row[j] = row[j]+row[j-1]
        return row
        