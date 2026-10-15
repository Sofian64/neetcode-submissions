class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range (len(board)) :
            ligne = set()
            col = set()
            for j in range (len(board)) :
                if board[i][j] in ligne:
                    return False
                elif (board[i][j]) != "." :
                    ligne.add(board[i][j])

                if board[j][i] in col:
                    return False
                elif (board[j][i]) != ".":
                    col.add(board[j][i])
        for i in range (0, 7, 3):
            for j in range (0, 7, 3):
                carre = set()
                for x in range (3):
                    for y in range (3):
                        if board[i+x][j+y] in carre:
                            return False
                        elif (board[i+x][j+y]) != "." :
                            carre.add(board[i+x][j+y])
        return True