"""
Generate a 4 digit random number
Accept a 4 digit number from user

if corresponding digit matches then increment cow by 1
else increment bull by 1
"""
import random
c=str(random.randint(1000,10000))
a=input("Enter a 4 digit number:\n")
cow=0
bull=0
for i in range(0,len(c)):
    if c[i]==a[i]:
        cow+=1
    else:
        bull+=1
print("Cow = ",cow)
print("Bull = ",bull)
print("generated number is :\n",c)