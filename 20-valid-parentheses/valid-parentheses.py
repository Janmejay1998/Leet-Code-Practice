class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        
        brac = {'(':')','{':'}','[':']'}

        for ele in s:
            if ele in brac:
                stack.append(brac[ele])
            elif not stack or ele != stack.pop():
                return False
            
        return not stack and len(s)%2 == 0
            
        
        