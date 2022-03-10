class Solution(object):
    def hammingDistance(self, x, y):
        x = bin(x)[2:]
        y = bin(y)[2:]
        count = 0
        if len(x) > len(y):
            y = int(len(x)-len(y)) * '0' + y
        elif len(x) < len(y):
            x = int(len(y)-len(x)) * '0' + x
        elif len(x) == len(y):
            pass
        
        for i in range(len(x)):
            if x[i] != y[i]:
                count += 1
                
        return count