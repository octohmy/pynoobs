# splitting a string into a list of words
# using the split() method
# and then printing the list
# and then printing the list in reverse order
# and then printing the list in alphabetical order
# and then printing the list in reverse alphabetical order

# create a string
from os import read


my_string = "This is a string of words. The SW1 exam is frightfully close. This string contains three sentences"

# print(f"Original string:\n{my_string}\n")
# .strip() removes leading and trailing whitespace
#  ^ it's the same as strip(" ")
split_by_spaces_one = my_string.strip()
split_by_spaces_two = my_string.split()

# split by full stop
split_by_full_stop = my_string.split(".")
# print(f"Split by full stop:\n{split_by_full_stop}\n")

# to split by character first we need to get each word
split_by_word = my_string.split()
# print(f"Split by word:\n{split_by_word}\n")

no_spaces_string = "HereIsAStringWithNoSpaces"
# print(f"String with no spaces:\n{no_spaces_string}\n")

# split by character
split_by_char = list(no_spaces_string)
# print(f"Split by character:\n{split_by_char}\n")

split_by_char_list = []

# the first iteration of the loop
# no_spaces_string[0] = "H"
# for char in no_spaces_string:
#     print(char)
#     split_by_char_list.append(char)
#     print(f"the current list is {split_by_char_list}")
    
# print(f"Split by character list:\n{split_by_char_list}\n")



# using split to break up a list of names
# f = open("./names_to_clean.txt", "r")
# r = f.read()

# names are separated by a comma and a space
# split by comma and space
# names = r.split(", ")

# print(f"Original list of names:\n{names}\n")
# print(f"Names now split by comma and space:\n{names}\n")

# accepted_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "

# cleaned_name_list = []

# for name in names:
#     cleaned_name = ""
#     for char in name:
#         if char in accepted_characters:
#             cleaned_name += char
#     print(cleaned_name)
#     cleaned_name_list.append(cleaned_name)
    
# print(f"Names now cleaned:\n{cleaned_name_list}\n")



vegetables = ["carrot", "potato", "lettuce", "tomato"]

# for veg in vegetables:
#     for char in veg:
#         print(char)

# age = 15

# while age < 18:
#     print("You're still too young to come in!")
#     print(f"You're just {age}")
#     print("Come back next year!")
#     # assume a year has passed
#     age += 1

# print("Welcome in")

satisfied = False

while satisfied is False:
    print("I can't get no")
    print("I can't get no, satisfaction")
    # satisfied_question = input("Are u satisfied?: (y/n)")
    # if satisfied_question == "y":
    #     satisfied = True
        
    satisfied = input("Are u satisfied? (y/n)") == 'y'
    
    print("thanks, come again tomorrow")
        