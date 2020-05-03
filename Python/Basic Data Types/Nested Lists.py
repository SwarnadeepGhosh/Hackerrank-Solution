'''
Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format
The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines; the first line contains a student's name, and the second line contains their grade.

Output Format
Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.
'''
# Initialising a empty list which will be multidimentional
lst=list()
# Taking input from user and store it as a 2D or Nested list
for i in range(int(input())):
    name = input()
    score = float(input())
    lst.append([name,score])

# Sort the list elements with the obtained marks taking the second sub element of each element as a sorting key with the help of lambda function. 
# Lambda function is a small anonymous function which only have one expression 
lst.sort(key=lambda x : x[1])

# Storing the first sub element(i.e. lowest grade) as lowest variable
lowest=lst[0][1]
#print(lowest)
# Initialising a empty list to store the names of second lowest grade
namelist=list()

# Storing the second lowest grade in secondlowest variable and break after found and stored
for i in range(len(lst)):
    if(lowest<lst[i][1]):
        secondlowest=lst[i][1]
        break

# Storing the name(s) of any student(s) having the second lowest grade
for i in range(len(lst)):
    if(secondlowest==lst[i][1]):
        namelist.append(lst[i][0])

# sorting the namelist alphabetically and print elements in new line
namelist.sort()
for ele in namelist:
    print(ele)

#print(lowest)
#print(secondlowest)
#print(lst)
#print(namelist)