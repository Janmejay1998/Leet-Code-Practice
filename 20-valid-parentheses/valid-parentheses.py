class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        
        par_dict = {'(':')','{':'}','[':']'}

        for ele in s:
            if ele in par_dict:
                stack.append(par_dict[ele])

            elif not stack or ele != stack.pop():
                return False

        # If Stack is empty and size of String is even    

        return not stack and len(s)%2 == 0
            
        
        