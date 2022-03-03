class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        count = 0
        for i in range(len(startTime)):
            li = [i for i in range(startTime[i], endTime[i]+1)]
            if queryTime in li:
                count += 1
        return count