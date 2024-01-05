class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = x
        rev = 0
        while x!=0:
            r = x % 10
            rev = rev * 10 + r 
            x = int(x / 10)
        if rev == num:
            return True
            