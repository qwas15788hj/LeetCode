from collections import Counter
class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        arr = []
        for i in range(lowLimit, highLimit+1):
            num = 0
            i = str(i)
            for j in range(len(i)):
                num += int(i[j])
            arr.append(num)
        
        answer = Counter(arr).most_common()
        
        return answer[0][1]