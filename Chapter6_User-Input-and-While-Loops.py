
# coding: utf-8

# In[2]:

# how the input() Function Works
message = input("Tell me something, and I will repeat it back to you: ")
print (message)


# In[3]:

#Writing Clear Prompts
name = input("Please enter your name: ")
print("Hello, " + name + "!")


# In[5]:

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")


# In[ ]:

#Using int() to Accept numerical Input
age = input("How old are you?")
age = int(age)
age >= 18


# In[ ]:

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou''ll be able to ride when you're a little order.")


# In[ ]:

#The Modulo Operator
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " +str(number)+ " is even.")
else:
    print("\nThe number " +str(number) + " is odd.")


# In[ ]:

#The While Loop in a Action
current_number = 1

while current_number <= 5:
    print(current_number)
    current_number +=1


# In[22]:

#Letting the User Choose When To Quit
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message =""
while message != 'quit':
    message = input(prompt)
    
    if message != 'quit':
        print(message)


# In[23]:

#Using a Flag
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    
    if message == 'quit' :
        active = False
    else:
        print(message)


# In[25]:

#Using break to Exit a Loop
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)
    
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")


# In[26]:

#Using continue in a Loop
current_number = 0
while current_number < 10:
    current_number +=1
    if current_number %2 == 0:
        continue
    print(current_number)


# In[ ]:

#Avoiding Infinite Loops
x = 1
while x <= 5:
    print(x)
    x +=1
#Use CTRL-C to stop infinite loops


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:







# In[ ]:




# In[ ]:





# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



