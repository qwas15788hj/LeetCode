class Solution(object):
    def validateStackSequences(self, pushed, popped):
        stack = []
        for i in pushed:
            stack.append(i)
            while len(stack) != 0 and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
            
        if len(stack) == 0:
            return True
        else:
            return False