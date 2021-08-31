#Given an integer n, return true if it is a power of four. Otherwise, return false.
#An integer n is a power of four, if there exists an integer x such that n == 4x.

n = 16

while n >= 4 :
    if (n % 4 > 0) :
        break
    n /= 4
print(f"{n == 1}")
