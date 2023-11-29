import time
from art import *


def countdown_timer(minutes = 1, seconds = 10):
    # convert minutes to seconds and add to seconds
    seconds += minutes * 60
    # loop through the seconds
    for i in range(seconds, 0, -1):
        # print the time left with x minutes and x seconds
        print(f"Time remaining: {i // 60} minutes, {i % 60} seconds")
    
        # wait one second
        time.sleep(1)
        # now that one second has passed, the loop will run again
        tprint("pyNOOBS", font="alligator", chr_ignore=False)
    
    # when the loop is done, print "Time's up!"
    print ("Time's upppp!")

countdown_timer(2)