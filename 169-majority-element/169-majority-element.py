from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        cnt = Counter(nums).most_common()
        for i in cnt:
            if i[1] > int(len(nums)/2):
                return i[0]