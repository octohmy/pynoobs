haystack = [1, 2, 3, "a", "b", "c", "junk","more junk",[1,2,3,4,5,6], "random junk", "needle", 3, 4, 5, 6]

def find_needle(haystack):
    # your code here
    # go through the list find the index of the word needle
    
    # prepare the final string to use in the print statement
    final_string = "found the needle at position "
    
    # for loop to go through each element and check if it's a needle or not
    # if it is a needle, concatenate the index to the final string
    
    for i in range(len(haystack)):
        if haystack[i]=="needle":
            final_string += str(i)
            
    print (final_string)
            
find_needle(haystack)
        