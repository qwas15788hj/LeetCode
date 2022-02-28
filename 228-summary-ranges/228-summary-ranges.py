class Solution(object):
    def summaryRanges(self, nums):
        answer = []
        count = 0
        
        if len(nums) == 0:
            return answer
        else:
            start = nums[0]
            for i in range(len(nums)):
                if start + count != nums[i]:
                    if start == nums[i-1]:
                        answer.append(str(start))
                    else:
                        answer.append(str(start)+"->"+str(nums[i-1]))
                    start = nums[i]
                    count = 1
                else:
                    count += 1

            if start == nums[-1]:
                answer.append(str(start))
            else:
                answer.append(str(start)+"->"+str(nums[-1]))

            return answer