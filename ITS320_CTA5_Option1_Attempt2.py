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

def rev_list_fun(x):
 rev_list = x[::-1]
 return rev_list

user_values = []
i = 0

user_values.append(input('Enter your first name: '))
user_values.append(input('Enter your last name: '))
user_values.append(input('Enter the name of your elementary school: '))

print('Original list: ', user_values)
print('Reverse list: ', rev_list_fun(user_values))

input('Press enter to close')