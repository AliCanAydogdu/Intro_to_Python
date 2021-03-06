If Statements
#A simple example
cars = ["audi", "bmw" , "subaru", "toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

#Conditional Tests
car = "bmw"
car == "bmw"#True
car = "subaru"
car == "bmw"#False

#Checking for inequality
requested_topping = "mushrooms"

if requested_topping != "pepper":
    print("Hold the pepper!")

#Checking Whether a Value Is in a List
requested_topping = ["mushrooms","onions","pineapple"]
"mushrooms" in requested_topping

#Checking Whether a Value Is Not in a List
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
     print(user.title() + ", you can post a response if you wish.")

#if-else Statements
age = 17
if age >= 18:
    print("You are old enough to vote!") 
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

#The if-elif-else Chain
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

#Using Multiple elif Blocks
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65: 
    price = 10
else:
    price = 5 
print("Your admission cost is $" + str(price) + ".")

#Omitting the else Block
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65: 
    price = 5
print("Your admission cost is $" + str(price) + ".")

#Testing Multiple Conditions
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings: 
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings: 
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings: 
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

#Using if Statements with Lists
#Checking for Special Items
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

# if there is no green pepper
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

#Checking That a List Is Not Empty
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

#Using Multiple Lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")  
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")



