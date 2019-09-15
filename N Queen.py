import copy

solutions=[]

def take_input():
    """Accepts the size of the chess board"""
    while True:
        try:
            size = int(input('What is the size of the chessboard? n = \n'))
            if size == 1:
                print("Trivial solution, choose a board size of at least 4")
            if size <= 3:
                print("Enter a value such that size>=4")
                continue
            return size
        except ValueError:
            print("Invalid value entered. Enter again")

def get_board(size):
    """Returns an n by n board"""
    board = [0] * size
    for ix in range(size):
        board[ix] = [0] * size
    return board


def print_solutions(solutions):
    """Prints all the solutions in user friendly way"""
    for sol in solutions:
        # print(sol)
        for row in sol:
            print(row)
        print()


def is_safe(board, row, col, size):
    """Check if it's safe to place a queen at board[x][y]"""
    # check row on left side
    for iy in range(col):
        if board[row][iy] == 1:
            return False
    # check top left side#往左上移动一次
    ix, iy = row, col
    while ix >= 0 and iy >= 0:
        if board[ix][iy] == 1:
            return False
        ix -= 1
        iy -= 1
    # check top bottom left side#往左下移动一次
    jx, jy = row, col
    while jx < size and jy >= 0:
        if board[jx][jy] == 1:
            return False
        jx += 1
        jy -= 1

    return True


def solve(board, col, size):
    """Use backtracking to find all solutions"""
    # base case
    # if col >= size:
    #     return

    for i in range(size):
        if is_safe(board, i, col, size):
            board[i][col] = 1
            if col == size - 1:
                add_solution(board)
                board[i][col] = 0
                return
            solve(board, col + 1, size)
            # backtrack
            board[i][col] = 0


def add_solution(board):
    """Saves the board state to the global variable 'solutions'"""
    saved_board = copy.deepcopy(board)#如果没有这个函数 那么这个board总是在变
    solutions.append(saved_board)


size = take_input()

board = get_board(size)

solve(board, 0, size)

print(solutions)

print_solutions(solutions)

print("Total solutions = {}".format(len(solutions)))