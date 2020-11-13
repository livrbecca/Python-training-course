def print_hello_world(name):
    print("Hello {}!".format(name))


print_hello_world("liv") #this is how you call it. enter argument here if any

#functions start with def, short for definition / define, then a function name
#explanatory function names

def print_hello(greeting, name="olivia"): #name has default value
    print("{0} {1}!".format(greeting, name))

print_hello(greeting="hey there")

def power(a, b):
    print(a ** b, a**b)

print(power(10,2))


def add_two_numbers():
    number1 = 10
    number2 = 50
    answer = number1 + number2
    print("{} plus {} is {}".format(number1, number2, answer))
add_two_numbers()