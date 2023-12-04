"""
import random
"""
def generate_square_board():
    square_board = [0, 0, 0, 0]
    

    """
    change square_board above to reflect the 2 X 2 board
    insert code here to generate a square board of 2 X 2 with zeros
    """
    return square_board

def print_board(square_board):
    """
    :param square_board:
    print the board as instructed
    """
    print(f"| {square_board[0]:2d}| {square_board[1]:2d} |")
    print(f"| {square_board[2]:2d}| {square_board[3]:2d} |")

    #    2x2 grid | 0| 0 |



import random
def generate_numbers(square_board):
    """
    :param square_board:
    generate the random numbers to replace all zeros on the board
    """
    def random_num_1_20():
        return random.randint(1, 20)
    
    square_board[0] = random_num_1_20()
    square_board[1] = random_num_1_20()
    square_board[2] = random_num_1_20()
    square_board[3] = random_num_1_20()
    
    return square_board

def calculate_win(square_board):
    message = " "
    """
    :param square_board: 
    determine a win
    message = "There is a win"
    message = "No win"
    """
    sum_of_all = square_board[0] + square_board[1] + square_board[2] + square_board[3]
    
    print(f"Sum: {sum_of_all}")
    
    if sum_of_all % 10 == 0:
        message = "There is a win"
    else:
        message = "No win"
    return (message)

"""
this part of the coding is for testing purposes only
"""
square_board = generate_square_board()
generate_numbers(square_board)
print_board(square_board)
message = calculate_win(square_board)
print(message)