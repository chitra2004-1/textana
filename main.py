n = int(input("Enter number of queens: "))
def solveQ(board, col):
    if col == n: [print(r) for r in board]; print(); return True
    for i in range(n):
        if all(board[i][x] == 0 for x in range(col)) and all(board[x][y] == 0 for x, y in zip(range(i, -1, -1), range(col, -1, -1))) and all(board[x][y] == 0 for x, y in zip(range(i, n), range(col, -1, -1))):
            board[i][col] = 1
            if solveQ(board, col + 1): return True
            board[i][col] = 0
    return False
if not solveQ([[0] * n for _ in range(n)], 0): print("No solution exists.")
