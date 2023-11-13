# let's talk about slicing
# slicing is a way to get a subset of a list
# we use the colon operator to slice
# list[start:end]

# let's create a list
my_list = [1, 2, 3, 4, 5]
my_list_sliced = my_list[1:3]

# print(my_list_sliced)

# we can also slice from the beginning

my_list_sliced = my_list[:3]
# print(my_list_sliced)

# we can also slice to the end
my_list_sliced = my_list[3:]
# print(my_list_sliced)

# we can also slice from the end
my_list_sliced = my_list[-3:]
# print(my_list_sliced)

# we can also slice from the end
my_list_sliced = my_list[:-3]
# print(my_list_sliced)

# default start is 0
# default end is the length of the list
# default step is 1

# we can also slice with a step
my_list_sliced = my_list[::2]
# print(my_list_sliced)

# we can also slice with a reverse
my_list_sliced = my_list[::-1]
# print(my_list_sliced)

# we can also slice with a reverse and a step
my_list_sliced = my_list[::-2]


# let's solve some anagrams
# an anagram is a word that is formed by rearranging the letters of another word
# for example: cinema is an anagram of iceman

anagram_one = "cinema"
anagram_one_solution = anagram_one[1:2] 
print(anagram_one_solution)

anagram_two = "dormitory"
# anagram_two_solution = 

