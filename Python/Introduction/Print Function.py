'''
(print without newline in Python)
Read an integer N.
Without using any string methods, try to print the following:
123...N
Note that "..." represents the values in between.
'''

N = int(input())
for i in range(N):
    print(i+1,end='')