#Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

num = 38
while (num >= 10):
    temp = 0
    while (num > 0):
        temp += num % 10
        num //= 10
    num = temp
print(num)
