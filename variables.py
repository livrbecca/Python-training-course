# booleans, intergers, floats, strings
#bool
#int
#float
#str

weight = 80
height = 1.8
print(80 / (1.8 * 1.8))
print (weight / (height * height))
# gives the same results
# variable names start with lower case, if its long you can use _ instead of spaces

highest_peak = "Everest"
print("the highest mountain is " + highest_peak)
highest_peak = "33333 meters high"
print("the highest mountain is " + highest_peak)


print(str(30)) #30
print(bool("")) #false
print(bool(0)) #false
print(bool(1))
print(int(True))
print(float(10)) # added .0
print(int(7.6)) # changed to 7
print(float("3.14"))
print(bool("False")) # evaluates to true, false can only be an empty string or 0


age = str(22) # needs to be a str as it wont print different data types
first_name = "olivia"
last_name = "walker"

print(first_name + " " + last_name + " " + age)
