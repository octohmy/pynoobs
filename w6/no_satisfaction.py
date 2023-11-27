# i can't get no satisfaction
# cos I try and I try and I try and I try
#  🥁🥁🥁🎸

#  while I can't get no satisfaction... what can one do
#  cause I try and I try and I try and I try

# for loop or while loop?

# for loop is for when you know how many times you want to loop, right?
# while loop is for when you don't know how many times you want to loop

# while i'm riding round the world and i'm doing this and i'm signing that 🥁🎸👅


# mini challenge 1: 
# write a while loop that prints out the lyrics to the song
# ask the user if they're satisfied
# only stop singing the song when the user is satisfied


# mini challenge 2:
# write a for loop to print the lyrics of yellow submarine 3 times
# extra challenge: print the lyrics of yellow submarine 3 times, but each time
# it prints, it prints a different colour submarine






# mini challenge 3:
# write a class called 'Burger' with the __init__ function
# it should have 2 attributes: 'name' and 'price'
# it should have 2 methods: 'get_name' and 'get_price'









































































































































import time
satisfied = False

while not satisfied:
    print("\nI can't get no")
    time.sleep(1)
    print("satisfaction")
    time.sleep(2)
    print("cos I try")
    time.sleep(1)
    print("I try and I try and I try")
    time.sleep(2)
    print("I can't get no, I can't get no")
    print()
    satisfied = input("Satisfied? (y/n): ").lower() == "y"
    print()












yellow_submarine_chorus = [
    "We all live in a yellow submarine",
    "Yellow submarine, yellow submarine"
]

number_of_choruses = 3  # How many times we want to sing the chorus

for _ in range(number_of_choruses):
    for line in yellow_submarine_chorus:
        print(line)
        time.sleep(2)  # Pause for effect
    print()  # Add a new line after each chorus












class Burger:
    def __init__ (self, name, price):
        self.name = name
        self.price = price
        
    def get_name(self):
        message = f"This burger is called {self.name}"
        print(message)
        return message
    
    def get_description(self):
        message = f"This burger is called {self.name} and it costs ${self.price}"
        print(message)
        return message

    def get_price(self):
        print(f"This burger costs ${self.price}")
        return self.price
    
Burger("Big Mac", 5.99).get_description()
