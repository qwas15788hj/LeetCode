class Solution(object):
    def arrayPairSum(self, nums):
        answer = 0
        nums.sort()
        for i in range(len(nums)):
            if i%2 == 0:
                answer += nums[i]
        return answer