class Solution:
    def romanToInt(self, s: str) -> int:
        
        # Making Dictionary of Roman to Number
        Roman_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        number = 0    #Initializing number variable

        for i in range(len(s)-1):          #Preventing loop from getting index out of bound

            # Checking if current Roman value is less than next Roman value

            if Roman_dict[s[i]] < Roman_dict[s[i+1]]: 
                number = number - Roman_dict[s[i]]

            else:
                number = number + Roman_dict[s[i]]
        
        number = number + Roman_dict[s[-1]]      # Adding last remaining element of the String

        return number