
# coding: utf-8

#Hello World
print("Hello World!")

#Variables
x = ("Hello")
print(x)

x = ("Monday")
print(x)
x = ("Tuesday")
print(x)

#Strings
#title()
name = "ali can"
print(name.title())

#uppercase and lowercase
name = "Ali can"
print(name.upper())
print(name.lower())

#Concatenation
first_name = "ali"
last_name = "can"
full_name = first_name.title() + " " + last_name
print(full_name)


#Adding whitespace to strings with tabs or newlines
#tab
print ("Python")
print ("\tPython")

#newline
print("Months:\nJanuary\nFebruary\nMarch")


#Stripping Whitespace
favorite_day = " Wednesday "
print (favorite_day)

#left stripping : lstrip()
#right stripping : rstrip()

favorite_day = favorite_day.lstrip()
favorite_day = favorite_day.rstrip()
print (favorite_day)



#Numbers
print(3+2)
print(3-2)
print(3*2)
print(3/2)


#str() function
age = 22
message = "Happy " + str(age) + "rd Birthday!"
print(message)

#Run this to see The Zen of Python
import this
