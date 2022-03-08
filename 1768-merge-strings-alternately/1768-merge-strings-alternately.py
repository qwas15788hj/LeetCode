class Solution(object):
    def mergeAlternately(self, word1, word2):
        answer = ""
        for i in range(min(len(word1), len(word2))):
            answer += word1[i]
            answer += word2[i]
            
        if len(word1) == len(word2):
            return answer
        elif len(word1) > len(word2):
            answer += word1[len(word2):]
            return answer
        elif len(word1) < len(word2):
            answer += word2[len(word1):]
            return answer