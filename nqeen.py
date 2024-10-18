n = int(input("Enter number of queens: "))
def solveQ(board, col):
    if col == n:
        for row in board:
            print(row)
        print()
        return True
    for i in range(n):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solveQ(board, col + 1):
                return True
            board[i][col] = 0
    return False

def isSafe(board, row, col):
    for x in range(col):
        if board[row][x] == 1:
            return False
    for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False
    for x, y in zip(range(row, n, 1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False
    return True

board = [[0 for x in range(n)] for y in range(n)]
if not solveQ(board, 0):
    print("No solution exists.")
