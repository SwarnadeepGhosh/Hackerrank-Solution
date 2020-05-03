'''
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
NOTE: String letters are case-sensitive.

Input Format
The first line of input contains the original string. The next line contains the substring.

Sample Input
ABCDCDC
CDC

Sample Output
2
'''
def count_substring(string, sub_string):
    c=0
    #looping each character in string
    for i in range(len(string)):
    	# checking if the substring is present or not
        if sub_string in string:
        	#if present, incerease count by 1
            c+=1
            #collecting the index of the first occurance position of the substring and reduce the string to search in further parts .
            index=string.find(sub_string)
            string=string[index+1:]
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)