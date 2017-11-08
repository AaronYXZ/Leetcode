class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        ## http://fisherlei.blogspot.com/2013/01/leetcode-rotate-image.html
        
        ## https://github.com/gavinfish/leetcode-share/blob/master/python/048%20Rotate%20Image.py
        


        
        size = len(matrix)
        
        for row in range(size-1):
            for column in range(size - row-1):
                matrix[row][column], matrix[size-1-column][size-1-row] = matrix[size-1-column][size-1-row], matrix[row][column]
        
        for row in range(size // 2):
            for column in range(size):
                matrix[row][column], matrix[size-1-row][column] = matrix[size-1-row][column], matrix[row][column]
