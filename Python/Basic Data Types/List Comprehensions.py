'''
You are given three integers x,y and z representing the dimensions of a cuboid along with an integer n. You have to print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n. Here, 
0<=i<=x, 0<=j<=y, 0<=k<=z

Input Format
Four integers  and  each on four separate lines, respectively.

Print the list in lexicographic increasing order.

Sample Input 0

1
1
1
2
Sample Output 0

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
'''
x = int(input())
y = int(input())
z = int(input())
n = int(input())

l=list()

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k!=n:
                l.append([i,j,k])

l.sort()
print(l)
        