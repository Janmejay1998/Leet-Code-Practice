class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        if "" in strs:
            return ""

        if len(strs) == 1:
            return strs[0]
        
        else:
            strs.sort()
            for i in range(len(strs[0])):
                if strs[0][i] != strs[-1][i]:
                    return res
                res += strs[0][i]      
        return res
            

        