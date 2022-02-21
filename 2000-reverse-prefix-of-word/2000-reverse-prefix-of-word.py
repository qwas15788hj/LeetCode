class Solution(object):
    def reversePrefix(self, word, ch):
        idx = -1
        for i in range(len(word)):
            if word[i] == ch:
                idx = i
                break
                
        if idx == -1:
            return word
        
        else:
            return word[:idx+1][::-1] + word[idx+1:]