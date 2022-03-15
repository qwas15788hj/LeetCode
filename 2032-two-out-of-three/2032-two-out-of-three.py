class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        arr = [0] *101
        answer = []
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        nums3 = list(set(nums3))
        for i in nums1:
            arr[i] += 1
        for i in nums2:
            arr[i] += 1
        for i in nums3:
            arr[i] += 1
        
        for i in range(len(arr)):
            if arr[i] > 1:
                answer.append(i)
                
        return answer