# string slicing
# showing two variables declared by comma separated values

first_name, last_name = input("Enter your full name: ").split()
print(f"Hello, {first_name} {last_name}")
print(f"Dear Dr. {last_name}... your PhD is fake.")

# recursive function
def reverse(s):
    if len(s) <= 1:
        return s
    else:
        return reverse(s[1:]) + s[0]


print(reverse("hello"))

# 4 spaces is the standard indentation in Python
# 4 spaces looks like 1 tab
# but, you must either choose spaces or tabs and stick with it
# Python 3 does not allow mixing of tabs and spaces

#reminder of params and arguments

# poorly written functions
# exampleL: 

# optional parameters
def greet(name, greeting="Hello"):
    print(greeting + ", " + name)
    print(f"{greeting}, {name}")


greet("John")
greet("John", "Howdy")

# notice the difference between the two print statements
# notice the placeholder in the second print statement
# the optional parameter must be the last parameter in the function definition
# if it's not changed in the function call, it will use the default value


def multiple_return_values():
    dict = {"a": 1, "b": 2, "c": 3}
    sum = 1 + 2
    # return sum

    return dict, sum, 1, 2, 3


print(multiple_return_values())
