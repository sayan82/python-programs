#Q7. Write a program to calculate the sum of digits of a given number.

n=int(input("Enter a number:\n"))
sum=0
while(n>0):
    r=n%10
    sum=sum+r
    n=n//10
print("The total sum of digits is:",sum)
