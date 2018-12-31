#Write a program to calculate the sum of first digit and last digit of a given number

a=input("Enter a number :\n")

for i in a:
    z=a[0]
    s=a[-1]
sum=int(z) + int(s)
print("The sum of first digit and last digit of a given number:\n",sum)