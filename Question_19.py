"""
Write a  program to accept three sides of a triangle as input and print whether the Trangle is valid or Not.
(The trangle is valid, if sum of each of the two sides is greater then the third side.)

"""
class Triangle:
    def check(self,a,b,c):
        if (a+b>c):
            print("triangle is valid")
        elif (b+c>a):
            print("triangle is valid")
        elif (c+a>b):
            print("triangle is valid")
        else:
            print("triangle is not valid")
t=Triangle()
a=int(input("enter the first side of a triangle"))
b=int(input("enter the second side of the triangle"))
c=int(input("enter the third side of the triangle"))
t.check(a,b,c)