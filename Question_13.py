"""
Write a program to calculate sum of elements of M*N matrix.
"""
m=int(input("Enter the matrix size(m):\n"))
n=int(input("Enter the matrix size(n):\n"))
print("the matrix is ",m,"x",n)
s=0
for i in range(0,m):
    for j in range(0,n):
        print("Enter ",i,", ",j)
        d=int(input("value:\n"))
        s=s+d
print("the sum of elements in matrix is:\n",s)