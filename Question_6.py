#Q6.Write a program to accept 5 names from user and store these names into an array sort these array element in alphabetical order.

list1=[]
z=True
while(z):
    n=input("Enter a name:\n")
    list1.append(n)
    a=input("do want to enter a name(y/n):\n")
    if a!="y":
        z=False
print("your list is:\n")
print(list1)
print("your sorted list is:\n")
for i in list1:
    list1.sort()
print(*list1)