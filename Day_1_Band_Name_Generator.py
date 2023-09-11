#printing to the console in python
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

# Debugging practice
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.") 

#Input function
print("What is your name?\n")
a = input()
print(len(a))

#Write a program that switches the values stored in the variables a and b.
# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
temp = a
a = b
b = temp

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)




#1. Create a greeting for your program.
print("Welcome to brand name generator!!")
#2. Ask the user for the city that they grew up in.
city_name = input("May I know which city did you grow up in?\n")
#3. Ask the user for the name of a pet.
pet_name = input("May I ask your pet name\n")
#4. Combine the name of their city and pet and show them their band name.
print("Your band name could be " +city_name +" "+pet_name)
#5. Make sure the input cursor shows on a new line:


# Solution: https://replit.com/@appbrewery/band-name-generator-end