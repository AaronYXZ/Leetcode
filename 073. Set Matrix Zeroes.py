'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
'''

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        ## http://fisherlei.blogspot.com/2013/01/leetcode-set-matrix-zeroes.html
        ## https://github.com/gavinfish/leetcode-share/blob/master/python/073%20Set%20Matrix%20Zeroes.py
        
        firstRow = firstColumn = False
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            if matrix[i][0] == 0:
                firstColumn = True
        for j in range(n):
            if matrix[0][j] == 0:
                firstRow = True
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        for i in range(1,m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if firstColumn:
            for i in range(m):
                matrix[i][0] = 0
        if firstRow:
            for j in range(n):
                matrix[0][j] = 0
                
