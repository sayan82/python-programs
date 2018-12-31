#Write a program to accept a string from user , delete all vowels from the string and display the result.

string = str.maketrans(dict.fromkeys('aeiouAEIOU'))
a=input("Enter the string:\n")
s=a.translate(string)
print(s)