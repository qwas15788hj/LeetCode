class Solution(object):
    def diStringMatch(self, s):
        front = 0
        end = len(s)
        answer = []
        
        for i in range(len(s)):
            if s[i] == "I":
                answer.append(front)
                front += 1
            else:
                answer.append(end)
                end -= 1
        answer.append(front)
        
        return answer