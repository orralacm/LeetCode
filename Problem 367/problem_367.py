#Given a positive integer num, write a function which returns True if num is a perfect square else False.

num = 14

n = 0
i = 2
a = 0

if num == 1 :
    print("True")
    a = 1
else :
    while i < num :
        n = num
        print(n)
        if n % i == 0 :
            n /= i
            print(n)
            if n / i == 1 :
                print("True") 
                a = 2
        i += 1
if a < 2 :
    print("False")
