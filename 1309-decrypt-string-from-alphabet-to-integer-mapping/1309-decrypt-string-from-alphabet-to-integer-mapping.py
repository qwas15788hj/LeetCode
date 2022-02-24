class Solution(object):
    def freqAlphabets(self, s):
        arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10#', '11#', '12#', '13#', '14#', '15#', '16#', '17#', '18#', '19#', '20#', '21#', '22#', '23#', '24#', '25#', '26#']
        arr.reverse()
        for i in range(len(arr)):
            s = s.replace(arr[i], chr(122-i))
        
        return s