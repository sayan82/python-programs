"""
Write a Program to Accept character and display its Ascii value and its Next and Previous Character.
"""
class Ltr:
    def Ascii(self,c):
        y=ord(c)
        nex=chr(ord(c)+1)
        pre=chr(ord(c)-1)
        print("{}={} next letter={} prev letter ={}".format(c,y,nex,pre))
l=Ltr()
c=input("enter a character:\n")
l.Ascii(c)