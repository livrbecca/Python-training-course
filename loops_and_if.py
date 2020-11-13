#my_shopping_cart = ["cake", "plates", "plastic forks", "juice", "cups"]
#for item in my_shopping_cart:
    #print(item)

#some_numbers = [1, 2, 3, 4, 5, 6, 7]
#for number in some_numbers:
    #print(number * 2)


# greater than 10 returns too high
# less than 0 too low
# between number = nothing, no code for it


is_morning = True

if is_morning:
    print("Good morning")
else:
    print("Hello")


number = input("Enter a number between 1 and 10: ")
number = int(number)  # Converts the input string to an integer
if number > 10:
    print("Too high!")
elif number <= 0:
    print("Too low!")
elif number >= 1 or number <= 10:
    print("Okay!")



# else:
#     print("Okay, great work!")
