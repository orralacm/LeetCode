#An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

#Given an integer n, return true if n is an ugly number.

n = 14

if (n == 1) :
    print("True")

else :
    while n > 1 :
        if (n % 2 == 0) :
            n //= 2
            continue
        elif (n % 3 == 0) :
            n //= 3
            continue
        elif (n % 5 == 0) :
            n //= 5
            continue
        else :
            print("False")
            break
    if n == 1 : print("True")
