class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        
        par_dict = {'(':')','{':'}','[':']'}    # Paranthesis Dictionary

        for ele in s:       
            if ele in par_dict:         # If opening bracket is in dictionary then append in Stack
                stack.append(par_dict[ele])        

            #If there is no opening bracket and current bracket not equal to Stack

            elif not stack or ele != stack.pop():    
                return False

        # If Stack is empty and size of String is even    

        return not stack and len(s)%2 == 0
            
        
        