
# coding: utf-8

# In[7]:

# A simple dictionary
alien_0 = {'color' : 'green', 'points' : 5}

print(alien_0['color'])
print(alien_0['points'])


# In[10]:

#Accessing values in a dictionary
alien_0 = {'color' : 'green', 'points' : 5}
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")


# In[13]:

#Adding New Key-Value Pairs
alien_0 = {'color' : 'green', 'points' : 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)



# In[15]:

#Starting with an Empty Dictionary
alien_0 = {}
alien_0['color'] ='green'
alien_0['points'] = 5
print(alien_0)


# In[21]:

#Modifying values in a dictionary
alien_0 = {'color' : 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0 = {'color' : 'yellow'}
print("The alien is now " + alien_0['color'] + ".")


# In[35]:

alien_0 ={'x_position' : 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
       x_increment = 1
elif alien_0['speed'] == 'medium':
       x_increment = 2
else:
     # This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment. 
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))




# In[36]:

#Removing Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)


# In[3]:

#A Dictionary of Similar Objects
favorite_languages ={
    'jen' : 'python',
    'sarah' : 'c',
    'edward': 'ruby',
    'phil' : 'python'
}
print("Sarah's favorite language is " + favorite_languages['sarah'].title() + '.')


# In[5]:

#Looping Through All Key-Value Pairs
user_0 ={
    'username' : 'efermi',
    'first' : 'enrico',
    'last' : 'fermi',
}

for key, value in user_0.items():
    print("\nKey: " +key)
    print("Value: " +value)


# In[10]:

favorite_languages ={
    'jen' : 'python',
    'sarah' : 'c',
    'edward': 'ruby',
    'phil' : 'python'
}
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")


# In[15]:

#Looping Through All the Keys in a Dictionary
favorite_languages ={
    'jen' : 'python',
    'sarah' : 'c',
    'edward': 'ruby',
    'phil' : 'python'
}
for name in favorite_languages:
    print(name.title())


# In[21]:

favorite_languages ={
    'jen' : 'python',
    'sarah' : 'c',
    'edward': 'ruby',
    'phil' : 'python'
}
friends =['phil', 'sarah']
for name in favorite_languages:
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")
if 'erin' not in favorite_languages: 
    print("Erin, please take our poll!")


# In[22]:

#Looping Through a Dictionary’s Keys in Order
favorite_languages ={
    'jen' : 'python',
    'sarah' : 'c',
    'edward': 'ruby',
    'phil' : 'python'
}

for name in sorted(favorite_languages):
    print(name.title()+ ", thank you for taking the poll. ")
    




# In[23]:

#Looping Through All Values in a Dictionary
favorite_languages ={
    'jen' : 'python',
    'sarah' : 'c',
    'edward': 'ruby',
    'phil' : 'python'
}
#values()
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())


# In[24]:

#set() for nonrepetitive
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()): 
    
    print(language.title())



# In[25]:

#Nesting
#A List of Dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2] 
for alien in aliens:
       print(alien)


# In[30]:

#range() 
# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}  
    aliens.append(new_alien)
# Show the first 5 aliens: xfor alien in aliens[:5]:
    print(new_alien)
print("...")
# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))


# In[31]:

# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range (0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
# Show the first 5 aliens:
for alien in aliens[0:5]:
    print(alien)
print("...")


# In[32]:

#Change yellows to reds
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15


# In[33]:

#A List in a Dictionary
# Store information about a pizza being ordered. 
pizza = {
       'crust': 'thick',
       'toppings': ['mushrooms', 'extra cheese'],
       }
# Summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " +
       "with the following toppings:")
for topping in pizza['toppings']: 
    print("\t" + topping)


# In[36]:

favorite_languages ={
    'jen': ['python','ruby'],
    'sarah': ['c'],
    'edward': ['ruby','go'],
    'phil': ['python','haskell'],
}
for name, languages in favorite_languages.items():
    print("\n" +name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())


# In[38]:

#A Dictionary in a Dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title()) 
    print("\tLocation: " + location.title())


# In[ ]:



