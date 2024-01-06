class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        lcp=""

        if "" in strs:         # Checking if list have [""]
            return ""           # Returning ""

        if len(strs) == 1:      # Checking if list have single element
            return strs[0]      # Returning that single element

        else:
            strs.sort()         # Sorting in Alphabetically order

            for i in range(len(strs[0])):       # Iterating on first element of sorted list
                if strs[0][i] != strs[-1][i]:   # Comparing first and last element of sorted list
                    return lcp
                lcp += strs[0][i]           #Storing Longest Common Prefix

        return lcp
            

        