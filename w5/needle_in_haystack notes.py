haystack = [1, 2, 3, "a", "b", "c", "junk", "needle","more junk",
            "needle", "random junk", "needle", 3, 4, 5, 6]


def find_needle_in_haystack(haystack):
    
    index_of_needles = []

    # add the index values of where the needles are
    for i in range(len(haystack)):
        if haystack[i] == "needle":
            index_of_needles.append(i)

    # prepare final message to use in print statement
    final_string = "Found the needle at position "

    '''
    - first, check if there are any needles to avoid an error

    - add the index of the needle to the final string and if there
    are more add 'and position ' and the index of the next needle
    '''
    
    if len(index_of_needles) == 0:
        print("No needles found in the haystack.")
        return "No needles found in the haystack."
        # returning here will quit the function and not run the rest of the code

    for i in range(len(index_of_needles)):
        if i == 0:
            final_string += str(index_of_needles[i])
        else:
            final_string += " and position " + str(index_of_needles[i])

    # print(index_of_needles)
    
    
    
    # something newwww! 
    # 🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈🌈
    # COLOURS!!
    
    bold = "\033[1m"
    underline = "\033[4m"
    yellow = "\033[33m"
    red = "\033[31m"
    green = "\033[32m"
    blue = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    white = "\033[37m"
    
    reset = "\033[0m"    
    
    print (final_string) 
    # Found the needle at position 7 and position 9 and position 11
    
    # print(f"Now with colours!!:\n{bold}{cyan}{final_string}{reset}")
    
    # randomise the colour of the text
    import random
    random_colour = random.choice([yellow, red, green, blue, magenta, cyan, white])
    # computer_choice = random.choice(['rock', 'paper', 'scissors'])
    # print(f"Now randomised:\n{bold}{underline}{random_colour}{final_string}{reset}")
    
    # randomise each character of the text
    randomised_final_string = ""
    for char in final_string:
        random_colour = random.choice([yellow, red, green, blue, magenta, cyan, white])
        randomised_final_string += random_colour + char
    
    random_bold = random.choice([bold, ""])
    random_underline = random.choice([underline, ""])
    
    print(f"Now randomised by character:\n{random_underline}{random_bold}{randomised_final_string}{reset}")
    
    return final_string

find_needle_in_haystack(haystack)
