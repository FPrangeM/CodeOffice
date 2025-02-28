class Solution:
    def convert(self, s: str, numRows: int) -> str:

        def indice_zigzag(colunas, indice):
            if colunas == 1:
                return 1 
            ciclo = 2 * (colunas - 1)
            resto = indice % ciclo
            return min(resto + 1, 2 * colunas - resto - 1)

        rows = {i: '' for i in range(1, numRows + 1)}

        for i, ls in enumerate(s):
            rows[indice_zigzag(numRows, i)] += ls

        return ''.join([row for row in rows.values()])