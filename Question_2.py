#Q2.Write a program to accept ‘n’ numbers from user , store these numbers into an array. Find out maximum and minimum number from an Array.¶

list=[]
z=True
while(z):
    n=int(input("Enter a number:\n"))
    list.append(n)
    a=input("do want to enter a number(y/n):\n")
    if a!="y":
        z=False
print("your list is:\n")
for i in list:
    print(i)
print("max is :\n",max(list),"\n min is:\n",min(list))