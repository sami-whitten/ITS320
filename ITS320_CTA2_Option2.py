print('********CAR DICTIONARY********')

user_dict = {}

key = 'CAR BRAND:'
value = input('Enter car brand: ')
user_dict[key] = value

key = 'CAR MODEL:'
value = input('Enter car model: ')
user_dict[key] = value

key = 'YEAR:'
value = input('Enter car year: ')
user_dict[key] = value

key = 'STARTING ODOMETER:'
value = input('Enter starting odometer reading: ')
user_dict[key] = value

key = 'ENDING ODOMETER:'
value = input('Enter ending odometer reading: ')
user_dict[key] = value

print("Car dictionary: ", user_dict)

x = input('press enter to close')
