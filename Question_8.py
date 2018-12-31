#Write a program to swap the values of two variables using Call by Reference.

a = int(input("Enter 1st number:\n"))
b = int(input("Enter 2nd number:\n"))
print("\nBefore swap 1st = %d and 2nd = %d" %(a, b))
a, b = b, a
print("\nAfter swaping 1st = %d and 2nd = %d" %(a, b))
print()