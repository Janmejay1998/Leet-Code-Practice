class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:           # Checking value is negative or positive 
            return False

        num = x             # Make a copy of original value
        rev = 0             # Assigning reverse variable to zero

        while x!=0:
            r = x % 10              # Storing remainder 
            rev = rev * 10 + r      # Reversing the value
            x = int(x / 10)         # Updating X value with each iteration
        
        if rev == num:      # Palindrome checking 
            return True
            