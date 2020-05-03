'''
You have a record of  students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer  followed by the names and marks for  students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.

Input Format
The first line contains the integer , the number of students. The next  lines contains the name and marks obtained by that student separated by a space. The final line contains the name of a particular student previously listed.

Output Format
Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

Sample Input 0
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output 0
56.00
'''
'''
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
'''
# Taking a empty list to store the data
record=list()

#taking all the inputs 
n = int(input())
for i in range(n):
    '''
    data=input().split()
    for i in range(1,4):
        data[i]=float(data[i])
    record.append([data])
    '''
    name, *marks=input().split() #taking everything as strings
    for i in range(len(marks)):
        marks[i]=float(marks[i]) #change the input numbers from string to float
    record.append([name,marks]) #append each name marks pair within record list
# Taking input the query name which avarage will be returned
query = input()

# Scans for the query name and prints its average
for i in range(4):
    if query==record[i][0]:
        ave=(record[i][1][0] + record[i][1][1] + record[i][1][2])/3
        break
print("%.2f" %ave)

    

