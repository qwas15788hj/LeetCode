class Solution(object):
    def findNumbers(self, nums):
        count = 0
        for num in nums:
            if len(list(str(num)))%2 == 0:
                count += 1
        return count