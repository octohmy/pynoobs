from art import *
# aprint("butterfly")
# tprint("pyNOOBS", font="alligator", chr_ignore=True)



haystack = [1, 2, 3, "a", "b", "c", "junk", "needle","more junk",
            "needle", "random junk", "needle", 3, 4, 5, 6]


def find_needle_in_haystack(haystack):
    
    index_of_needles = []
    print(index_of_needles)

    # add the index values of where the needles are
    for i in range(len(haystack)):
        if haystack[i] == "needle":
            index_of_needles.append(i)

    print(index_of_needles)
    # prepare final message to use in print statement
    final_string = "Found the needle at position "
    print(final_string)
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
    
    
    print (final_string)
    return final_string

find_needle_in_haystack(haystack)
