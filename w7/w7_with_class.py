# list of reindeers names

reindeers = ['Dasher', 'Dancer', 'Prancer', 'Vixen', 'Comet', 'Cupid', 'Donder', 'Blitzen']

# practice with for loop
# print "reindeer X is ready to fly"

# import time

# for reindeer in reindeers:
#     print(f"{reindeer} is ready to fly!!!")
#     time.sleep(1)




# naughty or nice list, with message
nice_list = ["Alice", "Mark", "Hannah", "Vic", "Bob", "Charlie"]
naughty_list = ["Colin", "Monica", "Sophie", "Dani", "Eve", "Mallory", "Trudy"]

import random
# choose a random name
# print a message saying something nice if they're on the nice list or something not nice if on the naughty list

# Plan:
    # 1) import random
import random

    # 2) create variable of random integers
    
# user_input_name = input("What is your name? ")
nice_list = ["Alice", "Mark", "Hannah", "Vic", "Bob", "Charlie"]
naughty_list = ["Colin", "Monica", "Sophie", "Dani", "Eve", "Mallory", "Trudy"]

# 3) create a variable to store the random name
random_name = random.choice(nice_list) or random.choice(naughty_list)
random_name = random.choice(nice_list and naughty_list)

# 4) if/else to check which list the random name is from
    # print a nice or naughty message
    
# if random_name in nice_list or user_input_name in nice_list:
#     print(f"{random_name} is on the nice list!")
# elif random_name in naughty_list:
#     print(f"{random_name} is on the naughty list!")
# else:
#     print("You're not on either list!\nSanta doesn't know who you are")









# while there are nights until christmas, print X number of sleeps until christmas
# when are there are no more sleeps, print "Merry Christmas!"

# HINT:
# while loops always contain something to check if the condition is true or false!!
# inside the while loop you want something to end the loop, otherwise it will run forever

# PLAN:
# 1) set up the variables ✅
# 2) set up the stopping condition✅
# 3) while loop✅
    # while var sleeps until christmas is greater than 0, print message✅
    # minus one from the sleeps until christmas variable✅
    # outside the while loop, print "Merry Christmas!"


# import time
# # sleep until xmas
# sleeps_remaining = 20

# while sleeps_remaining > 0:
#     print(f"There are: {sleeps_remaining} sleeps until Christmas!!!\n🎄🎅🎄🎅🎄🎅🎄🎅")
#     # minus one from sleeps remaining
#     sleeps_remaining -= 1
#     time.sleep(1)

# # christmas message
# print("Merry Christmas!!!!")




# my_string = "It's CHRISTMAS!!! 🎄🎅🎄🎅🎄🎅🎄🎅\nThis is a string of words. The SW1 exam is frightfully close. This string contains three sentences."

# split_string = my_string.split()
# print(f"My split string is:\n{split_string}")

# split_string_fullstop = my_string.split('. ')
# print(f"My split string is:\n{split_string_fullstop}")

# split_by_char = list(my_string)
# print(split_by_char)



# pull in names_to_clean, clean them, print them a list
# file = open('names_to_clean.txt', 'r')

# open the file, prepare the name list
with open("names_to_clean.txt", "r") as f:
    r = f.read()
    # splitting by a comma and a space
    names = r.split(", ")
    print(f"List of names:\n{names}")
    
string_of_accepted_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ- "

# prepare the cleaned list
cleaned_name_list = []

# for loop to go over each name
# create an empty string in prep to append to cleaned_name_list
# after checking the chars of the name, append the name to the cleaned_name_list

for name in names:
    cleaned_name = ""
    
    for char in name:
        if char in string_of_accepted_chars:
            cleaned_name += char
            
    print(f"cleaned name here is: {cleaned_name}")
    cleaned_name_list.append(cleaned_name)
    
print(f"The cleaned name list is now:\n{cleaned_name_list}")