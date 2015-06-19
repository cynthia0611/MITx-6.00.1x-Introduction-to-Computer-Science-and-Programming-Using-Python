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
    
