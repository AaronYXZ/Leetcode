'''

Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]


'''

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        result = []
        if n == 0:
            return result
        if n == 1:
            return [[1]]
        
        num = 1
        
        left, right, top, bottom = 0, n-1, 0, n-1
        
        result = [[0 for i in range(n)] for j in range(n) ]
        
        while left < right and top < bottom:
            for i in range(left, right):
                result[top][i] = num
                num+=1
            for j in range(top, bottom):
                result[j][right] = num
                num+=1
            for l in range(right, left, -1):
                result[bottom][l] = num
                num+=1
            for m in range(bottom, top, -1):
                result[m][left] = num
                num+=1
            left, right, top, bottom = left+1, right -1, top +1, bottom -1 
        
        if left == right and top == bottom:
            result[left][top] = num
        
        return result
