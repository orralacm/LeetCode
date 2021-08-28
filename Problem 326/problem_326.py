#Given an integer n, return true if it is a power of three. Otherwise, return false.
#An integer n is a power of three, if there exists an integer x such that n == 3^x.

n = 27

while n > 2:
    if n % 3 > 0 :
        print("False")
        break
    n /= 3
print(f"{n == 1}")
