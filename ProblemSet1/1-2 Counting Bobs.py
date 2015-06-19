##Counting Bobs
##
##Assume s is a string of lower case characters.
##
##Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
##
##Number of times bob occurs is: 2

def my_count(string, substring):
    string_size = len(string)
    substring_size = len(substring)
    count = 0
    for i in xrange(0,string_size-substring_size+1):
        if string[i:i+substring_size] == substring:
            count+=1
    print ("Number of times bob occurs is: " + str(count))
my_count(s,'bob')

