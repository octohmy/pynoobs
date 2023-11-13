# OOP
# OOPs, I did it again

# wtf is a class?

# a class is a blueprint for an object
# an object is an instance of a class

# an object is a thing that has attributes and methods (functions)
# an attribute is a variable that belongs to an object

#  OOP(s) I did it again uses objects to design applications and programs

# the object could be like 'car' and the attributes could be 'colour', 'make', 'model', 'year', etc. along with the actual values of these for example: red, ford, mustang, 1967

# the classes are like the blueprints for the objects
# for example the class 'car' allows for fields such as 'colour', 'make', 'model', 'year', etc.

# attributes are the variables that store the data for the object

# methods are the functions that are associated with the object, special functions within that class

# all a bit confusing, right, dw, it'll make sense soon

# let's make a class
# classes are defined with the 'class' keyword and use capitalisation

# it's called camel case, not because it's a camel, but because it's a camelCase 
    #  ^^^^^^^^
    # camelCaseExampleForYouAllHereToday
    # after the first word, each word is capitalised
    
# other naming conventions:
# snake_case
# kebab-case
# PascalCase


# anyway, classes use camelCase

class Car:
    def __init__ (self, colour, make, model, year):
        self.colour = colour
        self.make = make
        self.model = model
        self.year = year
        
    def drive(self):
        print("Vroom vroom")

