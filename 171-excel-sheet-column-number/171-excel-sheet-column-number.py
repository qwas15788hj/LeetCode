class Solution(object):
    def titleToNumber(self, columnTitle):
        result = 0
        for i in range(len(columnTitle)):
            result += (ord(columnTitle[::-1][i])-64) * (26**i)
            
        return result