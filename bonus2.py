"""
Accept a 6 digit number from user.
Let the computer Generate Random numbers till the generated random number matches with user input

Finally display total number of attempts made by computer to match the user input
"""

import random
count = 0
z=True
while (z):
    n = int(input("Enter a six digit number:\n"))
    if (n == random.randint(100000, 999999)):
        print("match found!!")
        count += 1
    else:
        count += 1
    c = input("not matched!!!!!!\ndo you wamt to try again?(y/n)\n")
    if (c != 'y'):
        z = False
        print("Exited")
print("Total number of attempt is", count)
