class Solution:
    def romanToInt(self, s: str) -> int:

        D = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        subs = ['IV','XL','CD','IX','XC','CM']

        # s="MCMXCIV"
        S = 0

        i=0
        while i < len(s):
            if (i < len(s)-1) and s[i:i+2] in subs:
                S+= D[s[i+1]] - D[s[i]] 
                i+=2
            else:
                S+=D[s[i]]
                i+=1

        return S