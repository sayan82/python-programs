"""Write a program to accept a string value from the user and accept a char value from the user and
and find out the total occurrence of char value in the string value.
"""


def count(s, c):
    res = 0

    for i in range(len(s)):
        if (s[i] == c):
            res = res + 1
    return res
str =input("Enter the string:\n")
c =input("Enter the character to find occurrence:\n")
print("Occurrence of",c,"is=",count(str, c))
