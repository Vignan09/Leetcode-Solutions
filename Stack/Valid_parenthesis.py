class Solution(object):
    def isValid(self, s):
        stack=[]
        for i in s:
            if i==")":
                if len(stack)>0 and stack[-1]=="(":
                    stack.pop()
                else:
                    return False
            elif len(stack)>0 and i=="]":
                if stack[-1]=="[":
                    stack.pop()
                else:
                    return False
            elif len(stack)>0 and  i=="}":
                if stack[-1]=="{":
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if len(stack)==0:
            return True
        else:
            return False            
