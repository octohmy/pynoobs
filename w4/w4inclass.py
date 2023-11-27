# hello = "hEllO world"

# # lowercase everything 
# print(hello.lower())

# # caps lock
# print(hello.upper())

# # make it a 
# print(hello.title())

#  we know we want to be using time so lets import time
import time
import math
import random 

def beers_on_the_wall(num_of_beers = 99):
    lyrics = ""
    
    for ex in range(num_of_beers, 0, -1):
        lyrics = f"{ex} beers on the wall, {ex} bottles of beer\nTake one down, pass it around, {ex-1} bottles of beer on the wall\n"
        
        print(lyrics)
        
        time.sleep(1)
        
    lyrics = "no more bottles of beer. go to the store, buy some more, 99 bottles of beer on the wall"
    
    print(lyrics)
    # return lyrics

beers_on_the_wall(10)