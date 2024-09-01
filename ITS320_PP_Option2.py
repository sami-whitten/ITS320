#-------------------------------------------
# Program Name: Module 8: Porfolio Project
# Author: Samantha Whitten
# Due Date: 8/4/2024
#-------------------------------------------
# Pseudocode: 
# define class house and attributes of the object
# define print list function which formats and lists the attributes of each house in the given list
# define get house info method which obtains all attributes of a house from a user, then creates and returns the new object with them
# declare empty list
# define main menu function which allows user to loop through options to view, add, and delete houses from the list
# call main menu function to run through options 
# option 1 allows user to view list of all houses entered then returns them to the main menu
# option 2 allows user to enter as many houses to the list as they would like, writing the list out each time
# with the newly added house and then returns them to the main menu when they no longer want to add any more houses
# option 3 allows user to delete as many houses from the list as they would like, rewriting the list for them each time and then returns them
# to the main menu when they are done. Option 0 closes the program. entering anything other than 1, 2, 3, or 0 will result
# in an error message that will ask the user for valid input. This is an error handling method used in each of the subscreens as well
#-------------------------------------------
# 
#-------------------------------------------

class house:
 def __init__(self,address,city,state,zip_code,sqft,model_name,sale_status):
  self.address = address
  self.city = city
  self.state = state
  self.zip_code = zip_code
  self.sqft = sqft
  self.model_name = model_name
  self.sale_status = sale_status
 
def print_list(house_list):
 i = 0
 while i < len(house_list):
  print("\n")
  print("House ",i+1)
  print("----------")
  print("Address        : ",house_list[i].address)
  print("City           : ",house_list[i].city)
  print("State          : ",house_list[i].state)
  print("Zip code       : ",house_list[i].zip_code)
  print("Square footage : ",house_list[i].sqft)
  print("Model name     : ",house_list[i].model_name)
  print("Sale status    : ",house_list[i].sale_status)
  print("\n")
  i = i+1

def get_house_info():
 address = input("Enter address: ")
 city = input("Enter city: ")
 state = input("Enter state: ")
 zip_code = int(input("Enter zipcode: "))
 sqft = int(input("Enter square footage: "))
 model_name = input("Enter model name: ")
 sale_status = input("Enter sale status: ")
 house1 = house(address,city,state,zip_code,sqft,model_name,sale_status)
 return house1

list = []

def main_menu():
 print("******************************************************************")
 print("---------------------------MAIN MENU------------------------------")
 print("******************************************************************")
 print("[1] List houses")
 print("[2] Add house")
 print("[3] Delete house")
 print("[0] Exit the program")
 print("--------------------")
 print("\n")
 
def main():
 
 main_menu()
 option = int(input("What would you like to do? "))

 while option != 0:
  if option == 1:
   #list house
   print("*LIST OF HOUSES*")
   print("----------------")
   print("\n")
   print_list(list)
   input("Press enter to return to main menu.")
   main_menu()
   option = int(input("What would you like to do? "))
  
  elif option == 2:
   #add house
   o = 'y'
   while o != 'x':
    if o == 'y':
     print("*ADD HOUSE*")
     print("----------")
     print("\n")
     house1 = get_house_info()
     list.append(house1)
     print_list(list)
     o = input("Would you like to add another house? ") 
    elif o == 'n': 
     break
    else:
     print("Error! Invalid key stroke.")
     o = input("Would you like to add another house? (y/n) ")
   input("Press enter to return to main menu.")
   main_menu()
   option = int(input("What would you like to do? "))
  
  elif option == 3:
   #delete house
   o = 'y'
   while o != 'x':
    if o == 'y':
     print("*DELETE HOUSE*")
     print("--------------")
     print("\n")
     print_list(list)
     x = int(input("Which house would you like to delete? "))
     x = x-1
     list.pop(x)
     print_list(list)
     x = x+1
     print("House ",x," has been removed.")
     o = input("Would you like to delete another house? ")
    elif o == 'n':
     break
    else:
     print("Error! Invalid key stroke.")
     o = input("Would you like to add another house? (y/n) ")
   input("Press enter to return to main menu.")
   print("\n")
   main_menu()
   option = int(input("What would you like to do? "))
  
  else:
   print("Invalid option.")
   print("\n")
   input("Press enter to return to main menu.")
   print("\n")
   main_menu()
   option = int(input("What would you like to do? "))

main()