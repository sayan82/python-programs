#Q1. Write A program to accept Four digit number from user and count zero , odd and even digits from the entered number

a=int(input("Enter a 4 digit number to check:\n"))
count=0
count1=0
count2=0
a1 = str(a)
for x1 in a1:
    x= int(x1)
    if x==0:
        count+=1
    elif x%2==0:
        count1+=1
    else:
        count2+=1
print("There are ",count,"zero present","there are",count2,"odd numbers","there are ",count1,"even numbers")

