class Solution(object):
    def findFinalValue(self, nums, original):
        nums.sort()
        for num in nums:
            if num == original:
                original *= 2
            if original > nums[-1]:
                return original
        return original