from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        cnt = Counter(nums).most_common()
        print(cnt[0])
        for i in cnt:
            if i[1] > int(len(nums)/2):
                return i[0]
        
        
        # set_nums = set(nums)
        # # for i in range(len(set_nums)):
        # #     if nums.count(set_nums[i]) > int(len(nums)/2):
        # #         return set_nums[i]
        # print(set(nums)[0])