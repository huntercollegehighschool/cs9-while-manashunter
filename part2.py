'''
***PART 2***

Write a program that prompts the user to enter a number. The program then prints "Hunter" the number of times the user entered. Use a while loop.

Example of what should appear when the program runs:

Times to print: 3
Hunter
Hunter
Hunter

'''
number = int(input('Times to print: '))
current_number = 0
while current_number < number:
  print("Hunter")
  current_number += 1
  