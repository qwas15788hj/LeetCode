class Solution(object):
    def checkString(self, s):
        if s == "".join(sorted(s)):
            return True
        else:
            return False