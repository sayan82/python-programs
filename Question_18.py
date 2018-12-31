"""
Write a program to calculate the x to the power y without using Standard functions.
"""
num=int(input("enter a number:\n"))
num1=int(input("enter the power:\n"))
a=1
for num1 in range (1,num1+1):
    a=(a*num)
print("the", num ,"to the power" ,num1,"is=\n",a)