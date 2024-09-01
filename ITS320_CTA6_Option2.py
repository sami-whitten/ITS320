#-------------------------------------------
# Program Name: Critical thinking Assignment 6 - Option 2
# Author: Samantha Whitten
# Due Date: 7/21/2024
#-------------------------------------------
# Pseudocode: 
# create class with attirbutes
# create funciton for filling lists
# create lists and variable for while loop
# append lists with user input numbers
# output lists as Cartesian products
#-------------------------------------------
# Program Inputs: 10 integers
# Program Outputs: the Cartesian product of the two lists
#-------------------------------------------

class Lists:
  def __init__(self, pos_1):
    self.pos_1 = pos_1

def fill_list():
 x = input('Enter a number: ')
 return x

list_1 = []
list_2 = []
i = 0
j = 0
k = 0

print("Let's fill the first list")
while j < 10: 
 list_1.append(Lists(fill_list()))
 j = j+1

print("And the now the second list")
while k < 10:
 list_2.append(Lists(fill_list()))
 k = k+1

j = 0
print("The Cartesian products of your lists:")
while j < len(list_1):
 while i < len(list_1):
  print("(",list_1[j].pos_1,",",list_2[i].pos_1,")")
  i = i+1
 i = 0 
 j = j+1

input("Press enter to close")
 