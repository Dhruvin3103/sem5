# import random
# rows = 5
# cols = 5
# grid =[[i * cols + j for j in range(cols)] for i in range(rows)]
# mines = [random.randint(0, 25) for _ in range(5)]
# for i in range(5):
#     print(grid[i])
#     print()
# # print(grid,mines)
import random

def print_board(board, revealed,win):
    size = len(board)
    print("   " + "  ".join(str(i) for i in range(size)))
    for i in range(size):
        print(i, end=" ")
        for j in range(size):
            if revealed[i][j] or win:
                print("|" + board[i][j], end=' ')
            else:
                print("| ", end=' ')
        print("|")
        print(" +" + "----" * size)

def initialize_board(size, num_mines):
    board = [[' ' for _ in range(size)] for _ in range(size)]
    mines = random.sample(range(size * size), num_mines)

    for mine in mines:
        row = mine // size
        col = mine % size
        board[row][col] = 'X'

    return board

def count_mines_around(board, row, col):
    size = len(board)
    count = 0

    for i in range(max(0, row - 1), min(size, row + 2)):
        for j in range(max(0, col - 1), min(size, col + 2)):
            if board[i][j] == 'X':
                count += 1

    return count

def count_false_elements(matrix):
    count = 0
    for row in matrix:
        for element in row:
            if not element:
                count += 1
    return count

def reveal(board, revealed, row, col,num_mines):
    
    if revealed[row][col]:
        return
    revealed[row][col] = True
    
    remaining = count_false_elements(revealed)
    if remaining == num_mines:
        print("You Win !! ")
        win = True
        print_board(board, revealed, win)
        exit()
    if board[row][col] == 'X':
        print("Game Over! You hit a mine.")
        win = False
        print_board(board, revealed, win)
        exit()

    mine_count = count_mines_around(board, row, col)
    if mine_count == 0:
        for i in range(max(0, row - 1), min(len(board), row + 2)):
            for j in range(max(0, col - 1), min(len(board[0]), col + 2)):
                reveal(board, revealed, i, j,num_mines)
    board[row][col] = str(mine_count)


size = 3
num_mines = 3

win = False
board = initialize_board(size, num_mines)
revealed = [[False for _ in range(size)] for _ in range(size)]
while not win:
    print_board(board, revealed, win)
    row = int(input(f"Enter row (0-{size-1}): "))
    col = int(input(f"Enter col (0-{size-1}): "))
    if not (0 <= row < size and 0 <= col < size):
        print("Invalid input. Row and column must be between 0 and 4.")
        continue
    reveal(board, revealed, row, col,num_mines)


