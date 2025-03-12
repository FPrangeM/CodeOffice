class Solution:
    def findValidPair(self, s: str) -> str:

        # count charmap
        D = {}
        for char in s:
            D[char] = D.get(char, 0) + 1

        # create pars
        pairs = []
        for i in range(len(s)-1):
            pairs.append(s[i:i+2])

        # validate pairs
        for pair in pairs:
            if (pair[0]!=pair[1]) and (D[pair[0]] == int(pair[0])) and (D[pair[1]] == int(pair[1])):
                # print(pair)
                return pair

        # print('')
        return ''