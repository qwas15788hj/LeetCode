class Solution(object):
    def finalPrices(self, prices):
        answer = []
        for i in range(len(prices)-1):
            discount = 0
            for j in range(i+1, len(prices)):
                if prices[i] >= prices[j]:
                    discount = prices[j]
                    break
            answer.append(prices[i]-discount)
        answer.append(prices[-1])
        
        return answer