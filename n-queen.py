def is_safe(board, row, col, n):
    # Check if there is a queen in the same row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def print_solution(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()

def solve_n_queens_util(board, col, n):
    if col == n:
        print_solution(board)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1

            res = solve_n_queens_util(board, col + 1, n) or res

            board[i][col] = 0  # Backtrack if placing a queen doesn't lead to a solution

    return res

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_n_queens_util(board, 0, n):
        print("No solution exists.")

# Example usage
n = 4  # Change this to the desired size of the chessboard
solve_n_queens(n)

