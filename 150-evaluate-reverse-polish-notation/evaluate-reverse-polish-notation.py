class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        if len(tokens)==1:
            return int(tokens[0])
        else:
            l=["+","-","/","*"]
            stack=[]
            for i in tokens:
                if i not in l:
                    stack.append(i)
                else:
                    if i=="+":
                        stack[-2]=int(stack[-1])+int(stack[-2])
                        stack.pop()
                    elif i=="*":
                        stack[-2]=int(stack[-1])*int(stack[-2])
                        stack.pop()
                    elif i=="-":
                        stack[-2]=int(stack[-2])-int(stack[-1])
                        stack.pop()    
                    elif i=="/":
                        stack[-2]=int(int(stack[-2])/int(stack[-1]))
                        stack.pop()    
            if stack[-1] not in l:
                return stack[-1]
            else:
                return stack[-1]    


                     