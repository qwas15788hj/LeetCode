from collections import Counter
class Solution(object):
    def repeatedNTimes(self, nums):
        counter = Counter(nums).most_common()
        return counter[0][0]