def print_solution(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print()

def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col]:
            return False
    
    # Check upper-left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j]:
            return False
    
    # Check upper-right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j]:
            return False

    return True

def solve_n_queens(board, row, n):
    if row == n:
        print_solution(board)
        return True  # return True to print only one solution, change to `False` to print all

    res = False
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            res = solve_n_queens(board, row + 1, n) or res
            board[row][col] = 0  # backtrack

    return res

def n_queens(n):
    board = [[0] * n for _ in range(n)]
    if not solve_n_queens(board, 0, n):
        print("No solution exists")

# Example: Solve for 4 queens
n_queens(4)
