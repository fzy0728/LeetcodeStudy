# coding:utf-8
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        #算法思路：首先对matrix转置，然后再对matrix中间列进行对称

        for i in xrange(len(matrix)):
            for j in xrange(i+1,len(matrix)):
                matrix[i][j] ,matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix)/2):
                matrix[i][j],matrix[i][len(matrix)-j-1] = matrix[i][len(matrix)-j-1],matrix[i][j]
        print matrix



