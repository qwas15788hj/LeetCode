class Solution(object):
    def minCostToMoveChips(self, position):
        add = 0
        even = 0
        for i in position:
            if i%2 == 0:
                even += 1
            else:
                add += 1
                
        return min(add, even)