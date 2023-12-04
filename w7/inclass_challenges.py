# days until christmas

# from datetime import datetime, timedelta
# import time

# # current date
# today = datetime.now()

# # christmas date for the current year
# christmas = datetime(today.year, 12, 25)

# # counting down days
# while today < christmas:
#     print(f"{(christmas - today)✅.days} days until Christmas!")
#     today += timedelta(days=1)
#     time.sleep(2)




# naughty or nice list

# import random

# nice_list = ["Alice", "Mark", "Hannah", "Vic", "Bob", "Charlie"]
# naughty_list = ["Colin", "Monica", "Sophie", "Dani", "Eve", "Mallory", "Trudy"]

# # name = input("Enter your name: ")
# random_name = random.choice(nice_list + naughty_list)

# if random_name in nice_list:
#     print(f"Congratulations, {random_name}! You're on the Nice list!")
# elif random_name in naughty_list:
#     print(f"Oops! Sorry, {random_name}!\nYou're on the Naughty list\nNo presents for you!")
# else:
#     print("You're not on any list. Screw you!")


# wishlist 

# wishlist = []

# print("Enter your Christmas wishlist items (type 'done' to finish):")

# while True:
#     item = input("> ")

#     if item.lower() == 'done':
#         break

#     wishlist.append(item)

# print("\nYour Christmas Wishlist:")
# for item in wishlist:
#     print(f"- {item}")


# for loops, design a christmas tree
height = int(input("Enter the height of the Christmas tree: "))

# Get the height of the Christmas tree from the user
height = int(input("Enter the height of the Christmas tree: "))

# Loop through each row of the tree
for i in range(height):
    # Print spaces before the stars to create the triangular shape
    for j in range(height - i - 1):
        print(" ", end="")
    
    # Print the stars for the current row
    for k in range(2 * i + 1):
        print("*", end="")
    
    # Move to the next line after printing each row
    print()


