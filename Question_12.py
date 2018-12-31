"""
Write a  program to accept a sentence from the user and reverse its each word.
"""

sentence =input("Enter the sentence you want to reverse by each word:\n")
print("reverse by each word is:\n",sentence[::-1])

"""
words = sentence.split(" ")
for i in words:
    s=" ".join(reversed(words))
words = s.split(" ")
for j in words:
    s1="".join(reversed(j))
    print(s1,end=' ')

"""
