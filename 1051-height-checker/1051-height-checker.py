class Solution(object):
    def heightChecker(self, heights):
        high = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != high[i]:
                count += 1
        return count