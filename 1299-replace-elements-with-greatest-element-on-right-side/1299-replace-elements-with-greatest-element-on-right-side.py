class Solution(object):
    def replaceElements(self, arr):
        answer = []
        for i in range(1, len(arr)):
            answer.append(max(arr[i:]))
        answer.append(-1)
        
        return answer