class Solution(object):
    def destCity(self, paths):
        a = set()
        b = set()
        for path in paths:
            a.add(path[0])
            b.add(path[1])
        return list(b-a)[0]