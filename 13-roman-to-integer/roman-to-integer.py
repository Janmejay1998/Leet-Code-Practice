class Solution:
    def romanToInt(self, s: str) -> int:
        Roman_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        val=0
        for i in range(len(s)-1):
            if Roman_dict[s[i]] < Roman_dict[s[i+1]]:
                val = val - Roman_dict[s[i]]
                print(val)
            else:
                val = val + Roman_dict[s[i]]
        val = val + Roman_dict[s[-1]]
        return val