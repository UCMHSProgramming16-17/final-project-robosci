def say_hello(someone):
    print("Hello", someone)
    
say_hello("matt")
say_hello("Devan")
say_hello("Sidney")

# now we do a print a message function twice
def print_a_message_twice(someone):
    print("I love to eat food and so does", someone)
    print("I love to eat food and so does", someone)
    
print_a_message_twice("Cady")

# using for loop
def print_five_times(message):
    for x in range(5):
        print(message)
        
print_five_times(3.14)

# more sophisticated for loop
def print_some_times(repretitions,message):
    for rep in range(repretitions):
        print(message)
        
print_some_times(100, "Good morning")

#input
def print_input_times(repretitions,message):
    for rep in range(repretitions):
        print(message)
        
print_input_times(int(input("how many times should I print it? ")), input("What's your message? "))


# going back to do now
inches = int(input("How many inches? ")) # What we had before

cm = inches * 2.54
print(inches, "inches is", cm, "centimeters. ")

# What we have now:
def in_to_cm(inches):
    cm = inches * 2.54
    print(inches, "inches is", cm, "centimeters. ")
    
in_to_cm(input("How many inches?", 5)