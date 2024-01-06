class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brac = {'(':')','{':'}','[':']'}
        close = {')':'(','}':'{',']':'['}

        if len(s)%2 == 1:
            return False

        if s[0] in close or s[-1] in brac:
            return False

        for ele in s:
            if ele in brac:
                stack.append(brac[ele])
            elif ele in close:
                if not stack or ele != stack.pop():
                    return False
            
            
        return not stack
            
        
        