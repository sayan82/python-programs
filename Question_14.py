"""
Write a program to accept ‘n’ numbers from user and store these numbers
into an array and count the number of occurrences of each number.
"""
from collections import Counter
z=[]
x=int(input("Enter the number of inputs u want to give"))
for y in range(x):
    a=int(input("Enter the number"))
    z.append(a)
x=Counter(z)
print(x)