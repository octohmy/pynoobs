# While loops are used to repeat a block of code until a condition is met
# For loops are used to repeat a block of code for a certain number of times

# Usually you'd use a while loop when you don't know how many times you want to repeat the code, and a for loop when you do know how many times you want to repeat the code


'''

While Loops:
The Infinite Pizza Loop

Write a program that keeps asking the user if they want another slice of pizza. If they say "yes", print a message saying they got another slice. If they say "no", exit the loop and print a message saying "No more pizza for you!"

Add funny comments or responses for each slice, like "Wow, slice number 27? You're a champion!... or something like that."

BONUS:
Add conditionals to check for the following:
- if the user enters 'y' instead of 'yes', it should print "I'll take that as a yes"
- if the user enters 'n' instead of 'no', it should print "I'll take that as a no"
- if the user enters anything other than 'yes' or 'no', it should print "I don't understand"

- respond with extra custom messages depending on how many slices the user has had, like "already 3 slices? maybe you should stop", or "wow, 5 slices? you must be hungry!", or "9 slices? you're a monster!" etc.

- if the user has had 10 slices, ask them if they want another slice. If they say "yes", tell them "I think you've had enough pizza for now", and exit the loop.

'''


'''
For Loops:

Write a program that prints out a list of things a lazy cat does in a day. For example, "Sleeping", "Eating", "Looking out the window", etc.

HINT:
- create a list of strings, e.g. ["Sleeping", "Eating", "Looking out the window", etc.]
- use a for loop to go through the list and print each item, "The lazy cat is now {item}."

BONUS:
- add a print statement at the beginning saying "The lazy cat is now awake!"
- add a print statement at the end saying "The lazy cat is now going to sleep!"

'''

'''

Parrot Repeater:
Let's create a parrot that repeats everything we say! 
We'll give it a phrase to repeat, and a number of times to repeat it.

Ask the user for a phrase, or allow our function to take a phrase as an argument.
Ask the user for a number of times to repeat the phrase, or allow our function to take a number as an argument.

Use a for loop to repeat the phrase the number of times specified.

CLUE:
- use the range() function to create a range of numbers to loop through



'''
import time

def parrot_repeater(phrase = "I love rock'n'roll", num = 3):
    for i in range(num):
        print(phrase)
        time.sleep(2) # sleep for 2 seconds, which means wait for 2 seconds before running the next line of code

parrot_repeater()


'''
More advanced for-loops:
The Joke Generator

Create a list of funny jokes and their punchlines. Use a loop to go through the list and print each joke, followed by its punchline.

BONUS:
- Add a print statement at the beginning saying "Welcome to the comedy show!"
- Add a print statement at the end saying "I'm here all week, folks!"
- Add a print statement after each punchline saying "hahahahaha!"

EXTRA BONUS:
- create another list of one liners and ask the user if they want more after your first loop, then print out a random one liner from your list and continue the loop until the user says they don't want any more jokes
- then print "London, you've been fantastic!! Goodnight! *mic drop*"
'''

import time

# sleep() method
print("Sleeping for 2 seconds...")
time.sleep(1)
print("1 second has passed...")
time.sleep(1)
print("Done sleeping!")

# localtime() method
local_time = time.localtime()
# print(f"Local time: {local_time}")

# strftime() method
#  %Y is year, %m is month, %d is day, %H is hour, %M is minute, %S is second, %I is hour (12 hour clock), %p is AM/PM

formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
formatted_12hr_time = time.strftime("%I:%M %p", local_time)

# print formatted time using strftime() method and f strings
# print(f"Formatted time: {formatted_time}")
# print(f"Formatted 12 hour time: {formatted_12hr_time}")


# make a timer function that counts down from x minutes and x seconds, printing out the time left every second
def countdown_timer(minutes = 1, seconds = 0):
    # convert minutes to seconds and add to seconds
    seconds += minutes * 60
    # loop through the seconds
    for i in range(seconds, 0, -1):
        # print the time left with x minutes and x seconds
        print(f"Time remaining: {i // 60} minutes, {i % 60} seconds")
        # wait one second
        time.sleep(1)
        # now that one second has passed, the loop will run again
    
    # when the loop is done, print "Time's up!"
    print ("Time's upppp!")

countdown_timer(0, 10)
# countdown_timer()

