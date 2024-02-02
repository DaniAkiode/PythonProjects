
def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c 
    return None, None


def is_valid(puzzle, guess, row, col):


    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    col_vals = []
    for i in range(9):
        col_vals.append(puzzle[i]col[i])

def solve_sudoku(puzzle):
    
    row, col = find_next_empty(puzzle)

    if row is None:
        return True 
    
    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):


