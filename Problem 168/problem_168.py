#Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

columnNumber = 33
output = ""
first = 0
second = 0

n = columnNumber + 64

if (n < 91) :
    print(chr(columnNumber + 64))
else :
    print(columnNumber)
    first = columnNumber / 26
    second = columnNumber % 26
    print(first)
    print(second)

