#-------------------------------------------
# Program Name: Critical thinking Assignment 4 - Option 1
# Author: Samantha Whitten
# Due Date: 7/7/2024
#-------------------------------------------
# Pseudocode: 
# ask user to put in five numerical values
# convert values from string to float
# add values together for total and output
# find average and output
# output max of user entered values
# output min of user entered values
# output each user entered value including 20 perc interest 
#-------------------------------------------
# Program Inputs: five numerical values
# Program Outputs: total, average, max, min, 20 perc interest for each value
#-------------------------------------------

user_values = []
i = 0
j = 0

while j < 5:
 user_values.append(float(input('Enter number: ')))
 j = j+1

print('Total of user entered values: ',sum(user_values))
print('Average of user entered values: ', ((sum(user_values))/(len(user_values))))
print('Maximum value of user entered values: ',max(user_values))
print('Minimum value of user entered values: ',min(user_values))

while i < len(user_values):
 x=(user_values[i])*1.2
 print('User entered value with interest: ',x)
 i = i + 1

input('Press enter to close')
