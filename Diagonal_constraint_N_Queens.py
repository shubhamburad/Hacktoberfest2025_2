def isSafe(queens, row, col):
    for r in range(row):
        c = queens[r]
        # Check same column
        if c == col:
            return False
        # Check diagonal attack constraints:
        # Descending diagonal
        if abs(c - col) == abs(r - row):
            return False
    return True

def solveNQueensUtil(queens, row, n, solutions):
    if row == n:
        solutions.append(queens[:])
        return
    for col in range(n):
        if isSafe(queens, row, col):
            queens[row] = col
            solveNQueensUtil(queens, row + 1, n, solutions)

def solveNQueens(n):
    solutions = []
    queens = [-1] * n
    solveNQueensUtil(queens, 0, n, solutions)
    return solutions

# Example to get and print all solutions for n=4
solutions = solveNQueens(4)
for sol in solutions:
    print(sol)
