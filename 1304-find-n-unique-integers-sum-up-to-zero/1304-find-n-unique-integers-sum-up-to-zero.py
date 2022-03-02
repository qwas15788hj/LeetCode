class Solution(object):
    def sumZero(self, n):
        answer = []
        for i in range(1, int(n/2)+1):
            answer.append(i)
            answer.append(-i)
        if len(answer) != n:
            answer.append(0)
        answer.sort()
        return answer