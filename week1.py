# WTF is python?
# the best way to get started is just by doing! 

# Notice how this text is slightly discoloured? They're called comments
# Use the # at the beginning to tell python to ignore this text
# Comments are for humans only

# Let's start from the top!! 

# Let's print something! 

print("My first print... Hello World!") # open your terminal, and type python3 week1.py

# Nice job! 

# Now, you try, print something out... print out your name.... 

# Type your code below:
print() # print your name here (don't forget the quotation marks)


# Now, let's try something a little more complicated
# Let's try to print out a sentence with a variable

# variables store information
# variables can store numbers, words, sentences, and more

my_first_var = "Hello World!" # this is a string variable
my_second_var = 1 # this is an integer variable, integer is a whole number
my_third_var = 1.0 # this is a float variable, float is a number with a decimal point
my_fourth_var = True # this is a boolean variable (True or False)
my_fifth_var = ["Banana", "Apple!"] # this is a list variable

# Create a variable called my_name, and store your name in it

# Type your code below:
my_name = "" # store your name in this variable

# eg. my_name = "Michael"

# Now, let's print out a sentence with your name in it

#  remove the # at the beginning below to make the code run
# print("My name is " + my_name + "!") # notice how we use the + sign to add the variable to the sentence

# ^^ this is an older way of doing it, there's an easier way to do it now, using f-strings
# f-strings are a newer way of formatting strings, and it's much easier to read
# f-strings are also faster than the older way of doing it
# you might have seen .format before, but f-strings are much easier to use
# remember f for format

# print(f"My name is {my_name}!") # notice how we use the {} to add the variable to the sentence

# Now, you try, print out a sentence with your name in it, using f-strings

# Enter your code below:
print() # print out a sentence with your name in it, using f-strings


# let's move onto using input

# instead of us coders typing the name we can ask the user

# user_name = input("What's your name?") # this will ask the user their name and store it to the variable

# print(user_name)

# Now, you try. Ask the user their name and store it to a variable
# then, print out a welcome message that includes your user's name (using f-strings)

# Code below:




# Great, so we should have something similar to...

# user_name = input("Please tell me your name: ")
# print(f"Welcome to UoB, {user_name}")

# Ask the user when they will graduate

# user_grad_year = \\Type your code here\\ # don't forget to un-comment this line

# Now change your welcome message to include their name and graduation year

# Attempt to give the user a welcome message, like as seen below
# "Welcome to the UoB, user_name!! Welcome to the class of user_grad_year"

# Let's extend the welcome message further by saying something like "you will have 3 years of fun and hard studies here"

# We know which year they graduate, and we know which year it is now, so we can calculate how many years they have left

current_year = 2023 # this is the current year, we can change this to any year we want

# let's make a calculation to find out how many years they have left

# we need to be very careful here, because when you use input() it will always save it as a string!

# does this make sense? "2028" - 2023 = ???
    # no, right, so we must make the answer of grad year to a number (a float or integer)

# let's try to convert the user_grad_year to an integer

# we use int()
    # put int() around the string variable of your grad_year variable
    # eg. age = "30"
        # age_int = int(age)
        # Now, age = 30 (a number)

# if you ever want to use maths on variables, make sure it's the right type! otherwise, you'll get an error

# years_left = \\Type your code here\\ # don't forget to un-comment this line

#HINT:
    # years_left = int(???) - ??? # what goes in the ???, think about what we just talked about


# Now, let's print out a welcome message that includes their name, graduation year, and how many years they have left

# something like this: "Welcome to the UoB, user_name!! Welcome to the class of user_grad_year. You will have the best years_left year(s) of your life here!!"

# Type your code below:




#HINT:
# print(f"Welcome to the UoB, {user_name}!! Welcome to the class of {user_grad_year}. You will have the best {years_left} year(s) of your life here!!")




# Let's move onto functions

# Functions are a way to group code together, so we can use it again and again
# It's like a  recipe, we can use it again and again to make the same thing

# Let's make a function that prints out a welcome message

# functions start with def, and then the name of the function, and then (), and then :

# def welcome_message():
    # user_name = input("Please tell me your name: ")
    # current_year = 2023
    # user_grad_year = input("When will you graduate?： ")
    # years_left = int(user_grad_year) - current_year
    # print(f"Welcome to the UoB, {user_name}!! Welcome to the class of {user_grad_year}. You will have the best {years_left} year(s) of your life here!!")

# Now, let's call the function
# welcome_message()

# Now, you try, make a function that asks the user for their name, and then prints out a welcome message. But, this time we are going to use parameters

# Parameters are like variables, but they are only used inside the function

# def welcome_message(user_name, user_grad_year):
    # current_year = 2023
    # years_left = int(user_grad_year) - current_year
    # print(f"Welcome to the UoB, {user_name}!! Welcome to the class of {user_grad_year}. You will have the best {years_left} year(s) of your life here!!")

# Now, when you call it you need to give it the parameters

# welcome_message("Michael", "2028")

# Notice how the first parameter is the user_name, and the second parameter is the user_grad_year. It can be called anything as long as you use it correctly

# For example:

# def sayHi(panda, cat):
    # print(f"Hi {panda}! Welcome to {cat}!")

# sayHi("Michael", "UoB")