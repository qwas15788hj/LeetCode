from collections import deque
class Solution(object):
    def sortArrayByParity(self, nums):
        answer = deque()
        for num in nums:
            if num%2 == 0:
                answer.appendleft(num)
            else:
                answer.append(num)
        return answer