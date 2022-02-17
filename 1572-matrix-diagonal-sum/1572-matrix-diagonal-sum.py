class Solution(object):
    def diagonalSum(self, mat):
        result = []
        for i in range(len(mat)/2):
            result.append(mat[i][i])
            result.append(mat[i][len(mat)-1-i])
            result.append(mat[len(mat)-1-i][i])
            result.append(mat[len(mat)-1-i][len(mat)-1-i])
        
        if len(mat)%2 != 0:
            result.append(mat[len(mat)/2][len(mat)/2])
        
        return sum(result)