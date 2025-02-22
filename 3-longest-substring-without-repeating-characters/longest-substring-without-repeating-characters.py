class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # N=0
        # for i in range(len(s)):
        #     n=0
        #     for f in range(i+1,len(s)+1):
        #         subs = s[i:f]
        #         if subs.count(subs[-1]) == 2:
        #             break
        #         N = max(N,len(subs))


        # return N

        char_index = {}  # Dicionário para armazenar o índice do último caractere visto
        start = 0       # Início da janela deslizante
        max_length = 0  # Comprimento máximo da substring encontrada

        for end, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                # Se o caractere já foi visto e está dentro da janela atual,
                # move o início da janela para a próxima posição após a repetição.
                start = char_index[char] + 1
            
            char_index[char] = end  # Atualiza o índice do caractere atual
            max_length = max(max_length, end - start + 1)  # Calcula e atualiza o comprimento máximo

        return max_length