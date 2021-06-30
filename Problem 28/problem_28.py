
haystack = "aaaa"
needle = "bbA"

y = haystack.count(needle)
print(y)

if (needle == "") :
    print("0")
elif (y == 0) :
    print("-1")
else :
    x = haystack.index(needle)
    print(haystack.index(needle))