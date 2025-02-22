class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        N=0
        for i in range(len(s)):
            n=0
            for f in range(i+1,len(s)+1):
                subs = s[i:f]
                if subs.count(subs[-1]) == 2:
                    break
                N = max(N,len(subs))


        return N