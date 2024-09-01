#-------------------------------------------
# Program Name: Critical thinking Assignment 5 - Option 1
# Author: Samantha Whitten
# Due Date: 7/14/2024
#-------------------------------------------
# Pseudocode: 
# declare function, list, and other variables
# ask for user input and store in list
# run through list on loop and reverse the string values provided by the user by calling the 
# rev_string_fun function
#-------------------------------------------
# Program Inputs: user first name, last name, and elementary school name
# Program Outputs: reverse of first name, last name, and elementary school
#-------------------------------------------

def rev_string_fun(x):
 return x[::-1]

user_values = []
i = 0
r = ''

user_values.append(input('Enter your first name: '))
user_values.append(input('Enter your last name: '))
user_values.append(input('Enter the name of your elementary school: '))

while i < len(user_values):
 r = rev_string_fun(user_values[i])
 print(r)
 i = i+1


input('Press enter to close')