import random
import time

DEAD = 0
LIVE = 1

def random_board(width, height):
    """Construct a random board with all cells randomly set.
    Parameters
    ----------
    width: the width of the board, in cells
    height: the height of the board, in cells
    Returns
    -------
    A board of dimensions width x height, with all cells randomly set to either
        DEAD or LIVE with equal probability.
    """
    board = dead_board(width,height)
    for x in range(board_height(board)):
        for y in range(board_width(board)):
            random_number = random.random()
            if random_number >= 0.5:
                cell_state = DEAD
            else:
                cell_state = LIVE

            board[x][y] = cell_state

    return board

def board_width(board):
    """Get the width of a board.
    Parameters
    ----------
    board: a Game board
    Returns
    -------
    The width of the input board
    """
    return len(board[0])

def board_height(board):
     """Get the height of a board.
    Parameters
    ----------
    board: a Game board
    Returns
    -------
    The height of the input board
    """
     return len(board)   

def dead_board(width, height):
    """Constuct an empty board with all cells set to DEAD.
    Parameters
    ----------
    width: the width of the board, in cells
    height: the height of the board, in cells
    Returns
    -------
    A board of dimensions width x height, with all cells set to DEAD
    """

    board = []

    for row in range(height):
        each_row = []
        for col in range(width):
            each_row.append(DEAD)
        board.append(each_row)

    return board

def print_board(board):
    """Displays a state by printing it to the terminal.
    Parameters
    ----------
    board: a Game board
    Returns
    -------
    Nothing - this is purely a display function.
    """
    for x in range(board_height(board)):
        for y in range(board_width(board)):
            if board[x][y] == DEAD:
                print("X", end = " ")
            else:
                print("O", end = " ")
        print()
    print()

def next_board_state(current_board):
    """Take a single step in the Game of Life.
    Parameters
    ----------
    board: the initial state of the Game board
    Returns
    -------
    The next state of the Game board, after taking one step for every cell in
    the previous state.
    """
    width = board_width(current_board)
    height = board_height(current_board)
    next_board = [[0 for x in range(width)] for y in range(height)]
    neighbors = [(-1, -1), (-1, 0), (-1, +1),
                   (0, -1),          (0, +1),
                  (+1, -1), (+1, 0), (+1, +1)]

    n_live_neighbors = 0 
    
    # Looping through each row
    for row in range(height):
        # Looping through each column
        
        for col in range(width):
            n_live_neighbors = 0
            # Loop through 8 neighbors
            for dx, dy in neighbors:
                i = row + dx
                j = col + dy

                if 0 <= i < height and 0 <= j < width:
                    if current_board[i][j] == LIVE:
                        n_live_neighbors += 1

            if current_board[row][col] == LIVE:
                if n_live_neighbors <= 1:
                    next_board[row][col] = DEAD
                elif n_live_neighbors <= 3:
                    next_board[row][col] = LIVE
                else:
                    next_board[row][col] = DEAD
            else:
                if n_live_neighbors == 3:
                    next_board[row][col] = LIVE

        
            

    return next_board
def run_forever(init_board):
    """Runs the Game of Life forever, starting from the given initial state.
    Parameters
    ----------
    init_state: the Game state to start at
    Returns
    -------
    This function never returns - the program must be forcibly exited!
    """
    next_board = init_board

    while True:
        print_board(next_board)
        next_board = next_board_state(next_board)

        time.sleep(1)



def main():
    width = 10
    height = 10
    start_board = random_board(width, height)
    run_forever(start_board)

if __name__ == "__main__":
    main()