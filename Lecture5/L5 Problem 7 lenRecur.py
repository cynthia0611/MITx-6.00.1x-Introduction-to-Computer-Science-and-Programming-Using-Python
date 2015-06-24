def lenRecur(aStr):
    count = 0
    if aStr == '':
        return 0
    else:
        return 1+ lenRecur(aStr[1:])

print lenRecur('a !! ')
