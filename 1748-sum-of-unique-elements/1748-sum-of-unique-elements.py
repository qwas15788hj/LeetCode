from collections import Counter
class Solution(object):
    def sumOfUnique(self, nums):
        counter = Counter(nums).most_common()
        answer = 0
        for count in counter[::-1]:
            if count[1] == 1:
                answer += count[0]
            if count[1] > 1:
                break
        return answer