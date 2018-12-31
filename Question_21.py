"""
Write a  program to create student structure having fields roll_no, stud_name, mark1, mark2,mark3.
Calculate the total and average of marks and arrange the records in  decending order of marks.
"""

lists=[]
list1=[]
student=int(input("enter the no of students:\n"))
for x in range(student):
    roll_no=int(input("enter the rollno:\n"))
    lists.append(roll_no)
    stud_name=input("enter the name:\n")
    lists.append(stud_name)
    marks1=int(input("enter the marks of the first subject:\n"))
    list1.append(marks1)
    marks2=int(input("enter the marks of the 2nd subject:\n"))
    list1.append(marks2)
    marks3=int(input("enter the marks of the 3rd subject:\n"))
    list1.append(marks3)
    Total=marks1+marks2+marks3
    Average=Total/3
    print("the total marks of the student is :\n")
    print(Total)
    print("the average marks of the student:\n")
    print(Average)
list1.sort(reverse=True)
print("the descending order of marks is :\n")
print(list1)
print("the names and roll no of students are:\n")
print(lists)
