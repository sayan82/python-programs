"""
Write a  program to accept basic salary from user. If basic salary>=5000 then hra=15% and da=150% of basic salary.
If basic salary<5000 then hra=10% and da=110% of basic salary .
Display the Gross salary.

"""

a=int(input("enter the basic salary:\n"))
if a>=5000:
    hra=(15*a)/100
    da=(150*a)/100
else:
    hra=(10*a)/100
    da=(110*a)/100
gs=hra+da+a

print("Basic salary is ",a)
print("Hra is ",hra)
print("Da is ",da)
print("Gross salary is ",gs)