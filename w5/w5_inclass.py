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

# let's make a human class and hardcode some values

class Human:
    name = "Michael"
    age = 21
    pros_and_cons = ["good at drinking tea", "bad at sleeping early"]
    
    # you can use self within the class to refer to the object itself, see example below
    
    # let's write a function within this class
    def speak(self):
        print("Hello, my name is", self.name) 
        # by using self.name we can use the name variable within the class
    
human = Human()
human.speak()



human.name = "Daniel"
# print(human.name)

# human.speak()

# let's step this up a gear with a constructor
# a constructor is a function that is called when the object is created
# it's called __init__ and it's a special function
# whenever the object is created, the __init__ function is called

# in the example below of class 'Car' whenever we use the class it'll automatically call the __init__ function, and we can pass in the values for the attributes, to give it a colour, make, model, year, etc.

# if you don't pass values in, it'll throw an error
    
# let's make a class called 'Car' with the __init__ function


# INIT

class Car:
    def __init__ (self, colour, make, model, year):
        self.colour = colour
        self.make = make
        self.model = model
        self.year = year
        
    def drive(self):
        # print("Vroom vroom, I'm in me mum's car")
        print(f"Vroom vroom, I'm in me mum's {self.colour} {self.make}")
        
    def honk_horn(self):
        # print("beep beep")
        print(f"beep beep, I'm a {self.make}, get out me way")
        

# let's make a car object
# we have to pass in the values for the attributes

lambo_car = Car("red", "Lamborghini", "Aventador", 2019)
ferrari_car = Car("yellow", "Ferrari", "F40", 1992)

# let's print the attributes of the car
# print(f"All the attributes of the lambo are:\n{lambo_car.__dict__}")
# print(f"The colour of the lambo is {lambo_car.colour}")
# print(f"The make of the lambo is {lambo_car.make}")

# i want to honk the horn of the lambo and drive it
# lambo_car.honk_horn()
# lambo_car.drive()


# let's make a class called 'Person' with the __init__ function
class Person:
    def __init__ (self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        
    def bmi(self):
        bmi = self.weight / (self.height ** 2)
        return bmi

    def bmi_category(self):
        bmi = self.bmi()
        if bmi < 18.5:
            return "underweight"
        elif bmi < 25:
            return "normal"
        elif bmi < 30:
            return "overweight"
        else:
            return "obese"
        
    def speak(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, my BMI is {self.bmi():.1f}, and I am {self.bmi_category()}")

# let's make a person object
# we have to pass in the values for the attributes

michael_person = Person("Michael", 31, 1.86, 75) 
# michael_person.speak()

tom_person = Person("Tom", 31, 1.76, 68)
tom_person.speak()