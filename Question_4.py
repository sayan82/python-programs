#Q4. Write a program to accept ‘n’ numbers from user , store these numbers into an array and sort the numbers of an array using function.

list1=[]
z=True
while(z):
    n=int(input("Enter a number:\n"))
    list1.append(n)
    a=input("do want to enter a number(y/n):\n")
    if a!="y":
        z=False
print("your list is:\n")
print(list1)
print("your sorted list is:\n")
for i in list1:
    list1.sort()
print(*list1)
