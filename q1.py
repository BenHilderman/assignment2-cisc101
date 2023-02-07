"""
This program displays a menu, asks user which item they want like to purchase, asks user if they want to tip, asks user how they want to tip (if agreed to tip), and then displays total price
Author:  Benjamin Hilderman
Student Number: 20374738
Date:  Sept 19, 2022
"""

# displaying the menu and instructions
userChoice = input('Items available for purchase: \n 1. Chicken Wrap $4.50 \n 2. Wings (10) $16.99 \n 3. Fries $4.59 \n 4. Meatball Sub $8.39 \n 5. Soup $2.95 \n Enter the number corresponding to the item that you would like to purchase: ')
if userChoice == '1' or userChoice == '2' or userChoice == '3' or userChoice == '4' or userChoice == '5': 
    tip = input('Would you like to tip? (Yes/No): ')
else: 
    print('You have made an invalid choice')
    exit()

# asks user how they want to tip (if user wants to tip)
if tip == 'Yes' or tip == 'yes': 
    typeOfTip = input('Would you like to enter a percentage to indicate the tip amount or would like to add a set amount for the tip? (Percent/Set Amount): ')

# sets tip amount to 0 and typeOfTipe to '' if user doesn't want to tip
elif tip == 'No' or tip == 'no': 
    tipAmount = 0
    typeOfTip = ''

else: 
    print('You have entered an invalid input')
    exit()

# setting the correct item price
if userChoice == '1': itemPrice = 4.50
elif userChoice == '2': itemPrice = 16.99
elif userChoice == '3': itemPrice = 4.59
elif userChoice == '4': itemPrice = 8.39
elif userChoice == '5': itemPrice = 2.95

# asks user what percent they want to tip if they chose percent
if typeOfTip == 'Percent' or typeOfTip == 'percent': 
    percentAmount = input('What percentage would you like to tip? ')
    tipAmount = (0.01 * float(percentAmount)) * itemPrice

# asks user what percent they want to tip if they chose percent
elif typeOfTip == 'Set Amount' or typeOfTip == 'set amount' or typeOfTip == 'Set amount' or typeOfTip == 'set Amount': 
    tipAmount = input('How much would you like to tip? ')
    tipAmount = float(tipAmount)

elif typeOfTip != '': 
    print('You have entered an invalid input')
    exit()

# calculates and displays total price
total = tipAmount + itemPrice * 1.05
print('The total will be $' + str(round(total, 2)))
