import random

print(random.randint(100,105)) # returns a random integer from a given range
print(random.randint(0,100))
print(random.randint(1,10))

print(random.random()) # returns a random float number 0 and 1
print(random.random()) # returned a different float number
print(random.random()) # returned a different float number

# variable containing the suggested sample list
fruits = ["apple", "banana", "cherry", "peach", "plum", "watermelon"]

print(random.choice(fruits)) # returns a random element from the given sequence
print(random.choice(fruits)) # returned a different fruit
print(random.choice(fruits)) # returned the same fruit as the first time 

print(random.choices(fruits, k = 10)) # returns a list with a random selection from the given sequence added the optional length of the returned list
print(random.choices(fruits, k = 12)) # returned a different list of twelve items with some of the items repeated
print(random.choices(fruits, k = 13)) # returned a different list from before but with twelve items and some of the items were repeated

print(random.sample(fruits,k=3)) # returns a given sample of a sequence with a size three for the returned list
print(random.sample(fruits,k=5)) # returned another sample of the list but this time with size five for the returned list no repeats
print(random.sample(fruits,k=2)) # returned another sample of the list but with a returned list of two items

random.shuffle(fruits) # takes a sequence and returns the sequence in a random order
print(fruits)          # returned the list of six items in a random order
random.shuffle(fruits) 
print(fruits)          # shuffled my list again and returned a different ordered list
random.shuffle(fruits)
print(fruits)          # shuffled my list once more and turned another ordered list no repeats just the six items I initally had