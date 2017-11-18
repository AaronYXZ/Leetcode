'''

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].

'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
    ## http://blog.csdn.net/linhuanmars/article/details/21667181 
    ## https://github.com/gavinfish/leetcode-share/blob/master/python/054%20Spiral%20Matrix.py
        result = []
        if matrix == []:
            return result
        
        left, right, top, bottom = 0, len(matrix[0])-1 ,  0, len(matrix)-1
        
        while left < right and top < bottom:
            for i in range(left, right):
                result.append(matrix[top][i])
            for j in range(top, bottom):
                result.append(matrix[j][right])
            for l in range(right, left, -1):
                result.append(matrix[bottom][l])
            for m in range(bottom, top, -1):
                result.append(matrix[m][left])
            left, right, top, bottom = left +1, right -1, top +1, bottom -1 
        
        if left == right and top == bottom:
            result.append(matrix[top][left])
        elif left == right:
            for i in range(top, bottom+1):
                result.append(matrix[i][left])
        elif top == bottom:
            for j in range(left, right+1):
                result.append(matrix[top][j])
        else:
            pass
        
        return result