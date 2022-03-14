from collections import Counter
class Solution(object):
    def kthDistinct(self, arr, k):
        count = Counter(arr).most_common()
        remove_set = []
        
        for i in count:
            if i[1] > 1:
                remove_set.append(i[0])
                
        answer = [i for i in arr if i not in remove_set]
        
        if len(answer) < k:
            return ""
        else:
            return answer[k-1]