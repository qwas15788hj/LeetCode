class Solution(object):
    def isSameAfterReversals(self, num):
        num = list(map(int, str(num)))
        if num[-1] == 0:
            if len(num) > 1:
                return False
            else:
                return True
        else:
            return True