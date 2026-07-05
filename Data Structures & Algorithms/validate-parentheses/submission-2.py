class Solution:
    def isValid(self, s: str) -> bool:
        k = []
        for i in s:

            if i == '(' or i == '{' or i == '[':
                k.append(i)
            else:
                if k == []:
                    return False

                if ( i == ')' and k[-1] == '(' )  or ( i == ']' and k[-1] == '[' ) or ( i == '}' and k[-1] == '{' ) :
                    k.pop()
                else:
                    return False

                    
        if k == []:
            return True
        return False

                # print("i = " + str(i))
                # print("k[-1] = " + str(k[-1]))
                
        
    


        