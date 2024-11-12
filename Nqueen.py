def solve_n_queen_bnb(n):#This function sets up and starts the branch and bound solution for the N-Queens problem with a given board size n
    # Initialize arrays to keep track of occupied columns and diagonals
    column_used = [False] * n           # Tracks occupied columns,column_used: This array tracks whether each column has a queen. column_used[i] is True if a queen is already placed in column i
    diag1_used = [False] * (2 * n - 1)   # Tracks "/" diagonals (index calculated as row + col)
    diag2_used = [False] * (2 * n - 1)   # Tracks "\" diagonals (row - col + n - 1)
    solutions = []                       #A list to store valid board configurations.
    board = [-1] * n                     # Represents queen positions by column in each row

    def solve(row):                      #The recursive solve function attempts to place queens row by row
        if row == n:                     # Base case: all queens are placed
            solutions.append(board[:])    # Add a valid solution
            return

        for col in range(n): #This loop tries placing a queen in each column of the current row.
            if not column_used[col] and not diag1_used[row + col] and not diag2_used[row - col + n - 1]:
                # Place the queen and mark the column and diagonals as used
                board[row] = col
                column_used[col] = diag1_used[row + col] = diag2_used[row - col + n - 1] = True

                solve(row + 1)            # Recur to place the next queen

                # Backtrack: remove the queen and unmark the column and diagonals
                column_used[col] = diag1_used[row + col] = diag2_used[row - col + n - 1] = False

    solve(0)  # Start solving from row 0
    return solutions #Call solve(0) to start placing queens from the first row, then return all solutions found

def print_solutions(solutions, n):
    for sol in solutions:
        print("Solution:")
        for row in range(n):
            line = ['.'] * n
            line[sol[row]] = 'Q'
            print(" ".join(line))
        print()

# Example usage
n = int(input("Enter the number of queens (n): "))
solutions = solve_n_queen_bnb(n)
print(f"\nTotal solutions for {n}-Queens problem: {len(solutions)}")
print_solutions(solutions, n)
