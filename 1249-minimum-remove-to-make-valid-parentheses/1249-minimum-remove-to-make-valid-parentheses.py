class Solution(object):
    def minRemoveToMakeValid(self, s):
        answer = [i for i in s]
        stack = []
        
        for i in range(len(answer)):
            if answer[i] == '(':
                stack.append(i)
            elif answer[i] == ')':
                if len(stack) != 0:
                    stack.pop()
                else:
                    answer[i] = ''
        
        if len(stack) != 0:
            for i in stack:
                answer[i] = ''
        
        return "".join(answer)