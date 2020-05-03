'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains n. The second line contains an array A[] of n integers each separated by a space.

Sample Input 0
5
2 3 6 6 5

Sample Output 0
5
'''
n = int(input())
#lst = map(int, input().split())
lst=input().split()

# Converting list elements to integer
for i in range(len(lst)):
    lst[i]=int(lst[i])

# Sorts the array in reverse order(maximum to minimum) 
lst.sort(reverse=True)

# Set the first(maximum) element as runnerup
runnerup=lst[0]

# collecting the second maximum value in runnerup variable
for i in range(n):
    if runnerup == lst[i]:
        continue
    elif runnerup > lst[i]:
        runnerup=lst[i]
        break

print(runnerup)
