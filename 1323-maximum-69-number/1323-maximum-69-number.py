class Solution(object):
    def maximum69Number (self, num):
        num_list = list(map(str, str(num)))
        print(num_list[0])
        
        for i in range(len(num_list)):
            if num_list[i] == '6':
                num_list[i] = '9'
                break
            
        return  "".join(num_list)