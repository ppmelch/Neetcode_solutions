class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charts = set()
        l = 0 
        res = 0 
        for r in range(len(s)):
            while s[r] in charts:
                charts.remove(s[l])
                l+=1 
            charts.add(s[r])
            res = max(res,r-l+1)
        return res
        
        