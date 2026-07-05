class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == '+' :
                    stack.append(stack.pop() + stack.pop())
                    print(stack)
                
            elif i == '-' :
                    a, b = stack.pop(), stack.pop()
                    stack.append(b - a) 
                    print(stack)
                
            elif i == '*' :
                    stack.append(stack.pop() * stack.pop())
                    print(stack)
                
            elif i == '/' :
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(float(b) / a))
                    print(stack)
            else:
                stack.append(int(i))
            

        return stack[0]

        # for i in tokens:
        #     print(i)
        #     if i != ('+' or '-' or '*' or '/'):
        #         stack.append(int(i))
        #         print(stack)

        #     else:
        #         if i == '+' :
        #             stack.append(stack.pop() + stack.pop())
        #             print(stack)
                
        #         if i == '-' :
        #             stack.append(stack.pop() - stack.pop()) 
        #             print(stack)
                
        #         if i == '*' :
        #             stack.append(stack.pop() * stack.pop())
        #             print(stack)
                
        #         if i == '/' :
        #             a, b = stack.pop(), stack.pop()
        #             stack.append(int(b / a))
        #             print(stack)

        #     return stack[0]
                     


        