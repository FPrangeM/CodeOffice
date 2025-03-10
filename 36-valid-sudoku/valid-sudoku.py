class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        # verify rows 
        for row in board:
            n_row = row[:]
            while '.' in n_row:
                n_row.remove('.')
            # print(len(n_row),len(set(n_row)))
            if len(n_row)!=len(set(n_row)):
                return False

        # verify column
        for i in range(len(board[0])):
            column= [row[i] for row in board]
            while '.' in column:
                column.remove('.')
            # print(len(column),len(set(column)))
            if len(column)!=len(set(column)):
                return False

        # verify block
        for i in [0,3,6]:
            for j in [0,3,6]:
                block = [board[i+k][j+z] for k in range(3) for z in range(3)]
                while '.' in block:
                    block.remove('.')
                # print(len(block),len(set(block)))
                if len(block)!=len(set(block)):
                    return False

        return True