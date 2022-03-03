class Solution(object):
    def sumBase(self, n, k):
        answer = ""
        while n > 0:
            n, mod = divmod(n, k)
            answer += str(mod)
        result = list(map(int, answer))
        return sum(result)