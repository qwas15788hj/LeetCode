class Solution(object):
    def selfDividingNumbers(self, left, right):
        answer = []
        for i in range(left, right+1):
            div_list = (list(str(i)))
            count = 0
            for div in div_list:
                if div != '0' and i%int(div) == 0:
                    count += 1
                    
            if count == len(div_list):
                answer.append(i)
        
        return answer