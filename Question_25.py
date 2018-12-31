"""
Write a  program to display whether the input character is a digit or alphabet.
"""

class Check:
    def find(self, ch):
        if (ch >= 'a' and ch <= 'z'):
            print("Its an alphabet")
        elif (int(ch) >= 0):
            print("Its an number")
        elif (int(ch) <= 0):
            print("Its an number but negative")


s = Check()
ch = input("Enter a charcater:\n")
s.find(ch)