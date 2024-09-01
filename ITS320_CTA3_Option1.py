#-------------------------------------------
# Program Name: Critical thinking Assignment 3 - Option 1
# Author: Samantha Whitten
# Due Date: 6/30/2023
#-------------------------------------------
# Pseudocode: 
# ask user to input car year
# determine car value using if else statements
# return approx value
# ask for input to close
#-------------------------------------------
# Program Inputs: car year
# Program Outputs: approx value
#-------------------------------------------

car_year = input('Enter car year: ')

car_year = int(car_year)

if car_year < 1962:
 print('ERROR')

if car_year > 1961 and car_year < 1965:
 print('Approximate value: $18,500')

if car_year > 1964 and car_year < 1969:
 print('Approximate value: $6,000')

if car_year > 1968 and car_year < 1972:
 print('Approximate value: $12,000')

if car_year > 1971 and car_year < 1976:
 print('Approximate value: $48,000')

if car_year > 1975 and car_year < 1981:
 print('Approximate value: $200,000')

if car_year > 1980 and car_year < 1986:
 print('Approximate value: $650,000')

if car_year > 1985 and car_year < 2013:
 print('Approximate value: $35,000,000')

if car_year > 2012 and car_year < 2015:
 print('Approximate value: $52,000,000')

if car_year > 2014:
 print('ERROR')


input('Press enter to close')

