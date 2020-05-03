'''
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Sample Input
this is a string   

Sample Output
this-is-a-string
'''
def split_and_join(line):
    # write your code here
    res=line.split()
    # Joining with a hiphen
    res='-'.join(res)
    return res

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)