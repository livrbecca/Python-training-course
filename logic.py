a = 1
b = 1

print(a == b) 
#comparison, returns true

#and/or

is_big = True
is_old = False

#(print(is_big or is_old)) # either to be true
#(print(is_big and is_old)) # need both to be true

c = "hello"
d = "not hello"

x = [1,2,3]
y = [2,4,5]
print(x == y) # false

x = [1,2,3]
y = [2,4,5]
print(x != y) #true

x = [1,2,3]
y = [2,4,5]
print(len(x) == len(y)) # true

print(1 * 10 == 10) # true

print((1*10 < 9) and (2 + 3 == 5)) #false

print((1*10 < 9) or (2 + 3 == 5)) # true
