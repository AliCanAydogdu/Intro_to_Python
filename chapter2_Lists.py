
# coding: utf-8

# In[5]:

#Here's a simple example of a list
bicycles = ['trek','canonndale','redline','specialized' ]
print(bicycles[0])
print(bicycles[0].title())


# In[6]:

#Index Positions Start at 0, Not 1
# At Index -1, python returns the last item, at index -2 second item from the end of list, so on.


# In[7]:

#Using Individual Values from the list
bicycles = ['trek','canonndale','redline','specialized' ]
message = "My first bicycle was a " + bicycles[2].title() + '.'
print(message)


# In[9]:

#Changing an item in the list
motorcycles =["Honda","Kawasaki","Yamaha"]
print(motorcycles)
motorcycles[0]="Ducati"
print(motorcycles)


# In[10]:

#Adding Elements to a List
#Appending Elements to the end of a list
motorcycles =["Honda","Kawasaki","Yamaha"]
print(motorcycles)
motorcycles.append("Ducati")
print(motorcycles)


# In[12]:

#Creating an empty list and adding elements with append
motorcycles = []
motorcycles.append("Honda")
motorcycles.append("Kawasaki")
motorcycles.append("Yamaha")
print(motorcycles)


# In[14]:

#Inserting Elements into a List
#You can add a new element at any position in your list by using the insert()
motorcycles =["Honda","Kawasaki","Yamaha"]
motorcycles.insert(0,"Ducati")
print(motorcycles)


# In[15]:

#Removing Elements from a list
#Removing an Item Using the del Statement
motorcycles =["Honda","Kawasaki","Yamaha"]
print(motorcycles)
del motorcycles[0]
print(motorcycles)


# In[19]:

#Removing an Item Using the pop() Method
motorcycles =["Honda","Kawasaki","Yamaha"]
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)


# In[21]:

#Popping Items from any position in a list
motorcycles =["honda","kawasaki","yamaha"]
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title())


# In[22]:

#Removing an Item by Value
motorcycles =["honda","kawasaki","yamaha"]
print(motorcycles)
motorcycles.remove("yamaha")
print(motorcycles)



# In[24]:

#Organizing a List
#Sorting a list permanently with the sort() method
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)
#Sorting the list in reverse alphabetical order
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort(reverse = True)
print(cars)


# In[28]:

# Sorting a list temporarily with the sorted() function
cars = ["bmw", "audi", "toyota", "subaru"]
print("Here is the original list")
print(cars)
print("\nHere is the sorted list")
print(sorted(cars))
print("\nHere is the original list again")
print(cars)


# In[30]:

#Printing a list in reverse order
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)
cars.reverse()
print(cars)


# In[31]:

#Finding the length of a list
cars = ["bmw", "audi", "toyota", "subaru"]
len(cars)


# In[ ]:




# In[ ]:



