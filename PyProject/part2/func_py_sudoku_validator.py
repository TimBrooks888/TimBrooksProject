# func_py_sudoku_validator.py
def func_py_sudoku_validator(board):
    def is_valid(block):
        nums = [num for num in block if num != 0]
        return len(nums) == len(set(nums))

    for row in board:
        if not is_valid(row):
            return False
    for col in zip(*board):
        if not is_valid(col):
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if not is_valid(block):
                return False
    return True

sample_board = [[5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0], [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3], [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5], [0, 0, 0, 0, 8, 0, 0, 7, 9]]

print(func_py_sudoku_validator(sample_board))
