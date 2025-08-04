class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        aberturas = []
        fechaduras = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for char in s:
            if char not in fechaduras: # se for abertura
                aberturas.append(char) 

            else: #se for fechadura
                ultima_abertura = aberturas.pop() if aberturas else '#'
                if ultima_abertura != fechaduras[char]:
                    return False

        return False if aberturas else True
