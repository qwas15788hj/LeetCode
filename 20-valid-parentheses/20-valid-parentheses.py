class Solution(object):  
    def isValid(self, s):
        self.s = s
        self.list = []
        result = True
          
        
        for i in self.s:
            if i =='(' or i == '[' or i == '{':
                self.list.append(i)
                
            elif len(self.list) != 0:
                if i == ')' and self.list[-1] == '(':
                    self.list.pop()
                elif i == ']' and self.list[-1] == '[':
                    self.list.pop()
                elif i == '}' and self.list[-1] == '{':
                    self.list.pop()
                else:
                    result = False
                    return result
            
            else:
                result = False
                return result
            
        if len(self.list) == 0:
            return result
        else:
            result = False
            return result