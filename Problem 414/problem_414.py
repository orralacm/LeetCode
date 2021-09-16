#Given an integer array nums, return the third distinct maximum number in this array.
#If the third maximum does not exist, return the maximum number.

nums = [3,2,1]

a = b = c = -float("inf")

for n in nums:
    if n in (a, b, c):
        continue
    if n > a: n, a = a, n
    if n > b: n, b = b, n
    if n > c: n, c = c, n

if c == -float("inf") :
    print(a)
else :
    print(c)
