import random
import time
import os
from turtle import clear

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()
grid_with_numbers = [1,2,3,4,5,6,7,8,9]

# random_choice = random.choice(choices)
# print(random_choice)

# player is either "X" or "O"
# to start, player is "X"

# something to help the while loop
player_x_score = 0
player_y_score = 0

def play_tic_tac_toe():
    global player_x_score, player_y_score
    choices = [1,2,3,4,5,6,7,8,9]
    grid = ["-","-","-","-","-","-","-","-","-"]
    active_game = True
    num_of_turns = 1
    player = "X"
    
    clear_terminal()

    while active_game:
        # choose randomly the position 
        position_at_play = 0
        if len(choices) > 0:
            position_at_play = random.choice(choices)
            # print(f"random position: {position_at_play}")
            # then remove the position from choices
            # print(f"Choices before removing: {choices}")
            choices.remove(position_at_play)
        else:
            # print("No more free squares to choose from")
            pass
        
        # print(f"Choices after removing: {choices}")
        
        # print(position_at_play)
        # print(f"Current options available are: {choices}")
        
        # make the position change to player's "X" or "O"
        # grid[position_at_play - 1] = player
        # print(grid[position_at_play - 1])
        # print(grid_with_numbers[position_at_play-1])
        # print (f"grid at this position currently contains: {grid[position_at_play-1]}")
        
        # change it to be the player's "X" or "O"
        # print(f"Player is currently: {player}")
        
        # COLOURS!!
        
        bold = "\033[1m"
        underline = "\033[4m"
        strikethrough = "\033[9m"
        yellow = "\033[33m"
        red = "\033[31m"
        green = "\033[32m"
        blue = "\033[34m"
        magenta = "\033[35m"
        cyan = "\033[36m"
        white = "\033[37m"
        
        reset = "\033[0m"
        
        player_colour = ""
        
        # if player == "X":
        #     player_colour = f"{bold}{yellow}"
        # elif player == "O":
        #     player_colour = f"{bold}{blue}"

        
        # change the value to be player
        grid[position_at_play-1] = player
        
        # grid_with_colours = grid
        # print(grid_with_colours)
        
        # grid_with_colours[position_at_play-1] = f"{player_colour}{player}{reset}"
        
        # after change
        # print (f"grid at this position after change to player contains: {grid[position_at_play-1]}")
        
        # print the full grid
        # print(grid)
        # make the formatted grid
        grid_formatted = f" {grid[0]} | {grid[1]} | {grid[2]} \n---+---+---\n {grid[3]} | {grid[4]} | {grid[5]} \n---+---+---\n {grid[6]} | {grid[7]} | {grid[8]} "
        
        # print formatted grid each move
        # print(grid_formatted)
        
        # now with colours
        grid_formatted_colours = f" {grid[0]} | {grid[1]} | {grid[2]} \n---+---+---\n {grid[3]} | {grid[4]} | {grid[5]} \n---+---+---\n {grid[6]} | {grid[7]} | {grid[8]} "

        for i in range(len(grid)):
            if grid[i] == "X":
                grid_formatted_colours = grid_formatted_colours.replace(grid[i], f"{blue}{grid[i]}{reset}")
            elif grid[i] == "O":
                grid_formatted_colours = grid_formatted_colours.replace(grid[i], f"{red}{grid[i]}{reset}")
                
        # print(grid_formatted_colours)
        
        
        # check for winning conditions
        # when winning condition is met active_game = False
        
        # winning message to display
        message = f"There is a win!\nPlayer {player} won!"
        
        # horizontal win
        horizontal_win = (grid[0] == grid[1] == grid [2] == "X") or (grid[0] == grid[1] == grid [2] == "O") or (grid[3] == grid[4] == grid[5] == "X") or (grid[3] == grid[4] == grid[5] == "O") or (grid [6] == grid[7] == grid[8] == "X") or (grid [6] == grid[7] == grid[8] == "O")
        
        # variable to track winning line
        winning_line = None

        # to see which indexes to strikethrough
        winning_indexes = []
        
        # horizontal win
        if grid[0] == grid[1] == grid[2] != "-":
            horizontal_win = True
            winning_line = "top_row"
            winning_indexes = [0,1,2]
        elif grid[3] == grid[4] == grid[5] != "-":
            horizontal_win = True
            winning_line = "middle_row"
            winning_indexes = [3,4,5]
        elif grid[6] == grid[7] == grid[8] != "-":
            horizontal_win = True
            winning_line = "bottom_row"
            winning_indexes = [6,7,8]
        
        # print(f"Horizontal win: {horizontal_win}")
        
        # vertical win
        vertical_win = (grid[0] == grid[3] == grid [6] == "X") or (grid[0] == grid[3] == grid [6] == "O") or (grid[1] == grid[4] == grid[7] == "X") or (grid[1] == grid[4] == grid[7] == "O") or (grid [2] == grid[5] == grid[8] == "X") or (grid [2] == grid[5] == grid[8] == "O") 
        
        # vertical win
        if grid[0] == grid[3] == grid[6] != "-":
            vertical_win = True
            winning_line = "left_column"
            winning_indexes = [0,3,6]
        elif grid[1] == grid[4] == grid[7] != "-":
            vertical_win = True
            winning_line = "middle_column"
            winning_indexes = [1,4,7]
        elif grid[2] == grid[5] == grid[8] != "-":
            vertical_win = True
            winning_line = "right_column"
            winning_indexes = [2,5,8]

        # print(f"Vertical win: {vertical_win}")
        
        diagonal_win = (grid[0] == grid[4] == grid [8] == "X") or (grid[0] == grid[4] == grid [8] == "O") or (grid[2] == grid[4] == grid[6] == "X") or (grid[2] == grid[4] == grid[6] == "O")
        
        # diagonal win
        if grid[0] == grid[4] == grid[8] != "-":
            diagonal_win = True
            winning_line = "left_diagonal"
            winning_indexes = [0,4,8]
        elif grid[2] == grid[4] == grid[6] != "-":
            diagonal_win = True
            winning_line = "right_diagonal"
            winning_indexes = [2,4,6]
            
        
        
                
        print(grid_formatted_colours)


        # print(f"Diagonal win: {diagonal_win}")
        
        # if either horizontal, vertical, or diagonal win - winner!
        # active_game = False
        if horizontal_win or vertical_win or diagonal_win:
            print(f"\n{message}")
            # print(f"winning line: {winning_line}")
            # print(f"winning indexes: {winning_indexes}")
            active_game = False
            if player == "X":
                player_x_score += 1
            else:
                player_y_score += 1
            # break
        elif num_of_turns == 9:
            print("There is a tie!")
            active_game = False

        # print(f"Num of turns so far: {num_of_turns}")
        num_of_turns += 1
        
        print(f"\n{underline}{bold}Scoreboard:{reset}\nPlayer X: {player_x_score}\nPlayer O: {player_y_score}\n")

        time.sleep(1)
        if active_game is True:
            clear_terminal()

    # then change player from X to O or O to X
        if player == "X":
            player = "O"
        else:
            player = "X"
    
    if active_game == False:
        print("Game over!")
        print("")
        def game_over_stuff():      
            play_again_question = input("Would you like to play again? (y/n): ")
            # print(play_again_question)

        
            if play_again_question.lower() == "n":
                print("No prob! See you later!!")
            elif play_again_question.lower() == "y":
                print("\nGreat, let's play again!")
                time.sleep(2)
                play_tic_tac_toe()
            else:
                print("Please choose either y/n/Y/N: ")
                game_over_stuff()
        
        game_over_stuff()

play_tic_tac_toe()
