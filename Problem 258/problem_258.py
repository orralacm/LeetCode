#Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

num = 38
n = str(num)
print(len(n))
a = 0

while len(n) > 1 :
    for i in range (len(n)) :
        a += int(n[i])
        print(a)
