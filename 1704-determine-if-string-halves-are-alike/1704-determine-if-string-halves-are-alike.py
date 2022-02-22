class Solution(object):
    def halvesAreAlike(self, s):
        arr = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        count1 = 0
        count2 = 0
        for i in range(len(s)/2):
            if s[i] in arr:
                count1 += 1
            if s[len(s)/2+i] in arr:
                count2 += 1
        if count1 == count2:
            return True
        else:
            return False