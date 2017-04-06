
#Looping through an entire list
magicians = ["alice","david","carolina"]
for magician in magicians:
    print(magician)

#A closer look at looping/Givinc meaningful names
for cat in cats:
for dog in dogs:

#Loop examples
magicians = ["alice","david","carolina"]
for magician in magicians:
    print(magician.title() + ", Hello!")
    print("How are you doing today?\n")

#Avoiding Indentation Errors
magicians = ["alice","david","carolina"]
for magician in magicians:
print(magician.title() + ", Hello!")#the print statement should be indented.


#Making numerical lists
#Using the range() function/ makes it easy to generate a series of numbers.
for value in range(1,5):
    print(value)

#Using range() to make a list of numbers with list() function
numbers = list(range(1,6))
print(numbers)

#Lising even numbers 1 to 10
even_numbers = list(range(2,11,2))
print(even_numbers)

#Listing of the first 10 square numbers
squares =[]
for value in range(1,11):
    square = value**2
    squares.append(square)
    
print(squares)
    


#Simple ststistics with alist of numbers
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

#List comprehensions
squares = [value**2 for value in range(1,11)]
print(squares)


#Working with part of a list
#Slicing a list
players = ["charles", "martina", "michael","florence","eli"]
print(players[1:4])
#From a number to the end
players = ["charles", "martina", "michael","florence","eli"]
print(players[3:])
#Printing the last three players
players = ["charles", "martina", "michael","florence","eli"]
print(players[-3:])

#Looping through a slice
players = ["charles", "martina", "michael","florence","eli"]
print("Here are the first three players on my team")
for player in players[:3]:
    print(player.title())


#Copying a list [:]
my_foods = ["pizza","falafel","carrot cake"]
friend_foods = my_foods[:]

print("my favorite foods are:")
print(my_foods)

print("my friend's favorite foods are:")
print(friend_foods)

#Tuples
#Defining
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

#Looping through all values in a tuple
dimensions = (200,50)
for dimension in dimensions:
    print(dimension)
    
#Writing over a tuple
dimensions = (200, 50) 
print("Original dimensions:") 
for dimension in dimensions:
       print(dimension)
dimensions = (400, 100) 
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
     
    



