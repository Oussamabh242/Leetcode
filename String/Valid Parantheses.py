class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<2 :
            return False
        stack = []
        for i in s : 
            if i == "(" or  i== "{" or i=="[" : 
                stack.append(i)
            else : 
                if len(stack)>0 :
                    if i ==")" and stack[len(stack)-1]=='(' :
                        stack.pop()
                    elif i =="]" and stack[len(stack)-1]=="[" :
                        stack.pop()
                    elif i == "}" and stack[len(stack)-1]=="{" :
                        stack.pop()
                    else :
                        return 
                else :
                    return False
        if(len(stack)==0) : 
            return True
        return False
                    
