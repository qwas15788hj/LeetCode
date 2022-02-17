from itertools import combinations_with_replacement

class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        for i in range(int(target/min(candidates)), 0, -1):
            a = list(combinations_with_replacement(candidates, i))
            for i in a:
                if sum(i) == target:
                    result.append(list(i))
        
        return result