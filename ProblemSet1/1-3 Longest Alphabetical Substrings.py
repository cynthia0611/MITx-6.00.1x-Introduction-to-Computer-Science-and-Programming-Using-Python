# Alphabetical Substrings

# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
# For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
# Longest substring in alphabetical order is: abc

# Solution 1:
def find(s):
    # return longest substring by printing this string
    # from the start to the end index using s[start:start + maxLen]
    # compare the temp length with the max length and store the bigger in maxLen
    # define variables as start = 0, length = 1, maxLen = 1
    # when reaching to the variable maxLen in the first time, it already finish the first round call

    start = 0
    length = 1
    maxLen = 1

    for i in range(len(s)-1):
        if s[i+1] > s[i]:
            length += 1
        else:
            length = 1
        if length > maxLen:
            maxLen = length
            start = i + 2 - maxLen
    return 'Longest substring in alphabetical order is: '+ s[start : start + maxLen]

print find('abcabcdopaqrstr')
    
# Solution 2:
 # get the largest number in a list
def maxNumInList(L):
    maxNum = L[0]
    for i in L:
        if i > maxNum:
            maxNum = i
    return maxNum
    
##L = [1,2,3,9,5,6,0]
##maxNumInList(L)

# get the length of each sequenced string with increasing order
# store it in a list
def maxNum(s):
    count = 1
    numlist = []
    point = [0]
    for i in range(1, len(s)):
        if s[i-1] <= s[i]:
            count += 1
        else:
            point.append(i)
            numlist.append(count)
            count = 1
    numlist.append(count)
    
    longestLen = maxNumInList(numlist) # the length of the longest string
    position = numlist.index(longestLen) # the position of the longest string in the max number list
    index = point[position] # the start index in the actual string

    ss = ''
    for i in range(index, index + longestLen): # print out the first longest string
        ss += s[i]

    print 'Longest substring in alphabetical order is: ' + ss

# s = 'a'
maxNum(s)

##print maxNumInList(maxNum(s))
