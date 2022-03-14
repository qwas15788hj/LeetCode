class Solution(object):
    def smallestEqual(self, nums):
        answer = []
        for i in range(len(nums)):
            if i%10 == nums[i]:
                answer.append(i)
        if len(answer) == 0:
            return -1
        else:
            return min(answer)