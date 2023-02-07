"""
This program gets the user's numerical grade and displays the equivalent letter grade
Author:  Benjamin Hilderman
Student Number: 20374738
Date:  Sept 19, 2022
"""

# user inputs numerical grade
numericalGrade = input('Enter your numerical grade to view your equivalent letter grade: ')
if numericalGrade.isnumeric():
    numericalGrade = round(int(numericalGrade))
else:
    print('Your value is invalid')
    exit()

# checks if the grade is above 100 and proceeds to go through the elif statements until the correct grade is found
if numericalGrade > 100: 
    print('Your value is out of range')
    exit()
elif numericalGrade >= 90: print('A+')
elif numericalGrade >= 85: print('A')
elif numericalGrade >= 80: print('A-')
elif numericalGrade >= 77: print('B+')
elif numericalGrade >= 73: print('B')
elif numericalGrade >= 70: print('B-')
elif numericalGrade >= 67: print('C+')
elif numericalGrade >= 63: print('C')
elif numericalGrade >= 60: print('C-')
elif numericalGrade >= 57: print('D+')
elif numericalGrade >= 53: print('D')
elif numericalGrade >= 50: print('D-')
elif numericalGrade >= 0: print('F')
else: 
    print('Your value is out of range')
    exit()
