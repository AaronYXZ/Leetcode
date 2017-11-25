'''

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1], [1,1]]
        if numRows == 0:
            return []
        elif numRows <= 2:
            return result[:numRows]
        oldRow = [1,1]
        for i in range(2, numRows):
            newRow = [1 for _ in range(i+1)]
            for j in range(1, i):
                newRow[j] = oldRow[j-1] + oldRow[j]
            result.append(newRow)
            oldRow = newRow
        return result