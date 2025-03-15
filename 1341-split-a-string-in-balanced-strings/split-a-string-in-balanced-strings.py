class Solution:
    def balancedStringSplit(self, s: str) -> int:


        D={}
        subs=''
        n=0

        for l in s:

            D[l] = D.get(l,0)+1
            subs+=l
            
            if D.get('L',0) == D.get('R',0):
                s = s.removeprefix(subs)
                subs = ''
                n+=1



        return n