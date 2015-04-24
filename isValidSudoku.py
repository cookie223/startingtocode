#Input example
blk = [['.' for i in range(9)] for i in range(9)]
blk[0][0] = 5
blk[0][1] = 3
blk[0][4] = 7
blk[1][0] = 6
blk[1][3] = 1
blk[1][4] = 9
blk[1][5] = 5
blk[2][1] = 9
blk[2][2] = 8
blk[2][7] = 6
blk[3][0] = 8
blk[3][4] = 6 
blk[3][8] = 3
blk[4][0] = 4
blk[4][3] = 8
blk[4][5] = 3
blk[4][8] = 1
blk[5][0] = 7
blk[5][4] = 2
blk[5][8] = 6
blk[6][1] = 6
blk[6][6] = 2
blk[6][7] = 8
blk[7][3] = 4
blk[7][4] = 1
blk[7][5] = 9
blk[7][8] = 5
blk[8][4] = 8
blk[8][7] = 7
blk[8][8] = 9
#blk[2][2] = 5

for i in range(9):
    print blk[i]


def checkrow(n, board):
    elen = 0
    eleset = {'head', }
    for i in range(9):
        if not board[n][i] == '.':
            elen += 1
            eleset.add(board[n][i])
    if elen == len(eleset) - 1:
        return True
    else:
        return False


def checkcol(n, board):
    elen = 0
    eleset = {'head', }
    for i in range(9):
        if not board[i][n] == '.':
            elen += 1
            eleset.add(board[i][n])
    if elen == len(eleset) - 1:
        return True
    else:
        return False


def checkM(n, board):
    elen = 0
    eleset = {'head', }
    for i in range(3 * int(n//3), 3 * int(n//3) + 3):
        for j in range(3 * int(n % 3), 3 * int(n % 3) + 3):
            if not board[i][j] == '.':
                elen += 1
                eleset.add(board[i][j])
    if elen == len(eleset) - 1:
        return True
    else:
        return False


def isValidSudoku(board):
    'A partially filled Sudoku can be valid while not soluable'
    for i in range(9):
        if not checkcol(i, board):
            return False
        if not checkM(i, board):
            return False
        if not checkrow(i, board):
            return False
    return True


print isValidSudoku(blk)
