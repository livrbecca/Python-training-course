empty_list = []
list_of_numbers = [0, 1, 2, 3, 4, 5]

# print(empty_list)
# print(len(empty_list))
# print(len(list_of_numbers))

my_shopping_list = ["apple", "pineapple", "mango", "tea", "popcorn"]
# print(my_shopping_list[-2]) #minus counts backwards

# print(my_shopping_list[4])

my_fave_fruits = ["mango", "kiwi", "pears"]

my_fave_fruits.append("raspberry")

# print(my_fave_fruits)

animals = ['koala', 'cat', 'dog', 'rabbit']

animals.append("fish")
animals.append("bunny")
animals.append("tiger")


animals.insert(100, "dragon")  # does not add 100 dragons

animals[0] = "myself"

removed_animal = animals.pop()  # pop removes the last

# print(animals)
#print(removed_animal, " has been removed")
#print("new animal list is:", animals)

result = animals.pop(2)
#print(result, animals)

nums = [3, 56, 1, 55, 2, 4]
nums.sort()
# print(nums)

square = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#print(square[1])
#print(square[1][1])
