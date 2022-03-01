class Solution(object):
    def countBits(self, n):
        answer = []
        for i in range(n+1):
            answer.append(list(bin(i)[2:]).count('1'))
            
        return answer