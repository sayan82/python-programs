"""
Write a program to calculate  X^(Y+Z) .
"""

class Power:
    def check(self, a, b, c):
        print("the number after evaluation is", (a ** (b + c)))


gk = Power()
x = int(input("Enter a number(X):\n"))
m = int(input("Enter a number(Y):\n"))
p = int(input("Enter a number(Z):\n"))
gk.check(x, m, p)
