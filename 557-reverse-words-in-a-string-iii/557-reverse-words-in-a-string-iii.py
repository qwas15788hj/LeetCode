class Solution(object):
    def reverseWords(self, s):
        result = []
        s = s.split(" ")
        for i in s:
            result.append(i[::-1])
            result.append(" ")
            
        return "".join(result[:len(result)-1])