from collections import Counter

class Solution(object):
    def areOccurrencesEqual(self, s):
        a = Counter(list(s)).most_common()
        cnt = a[0][1]
        for i in a:
            if i[1] != cnt:
                return False
        return True