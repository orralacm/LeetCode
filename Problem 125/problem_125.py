s = "A man, a plan, a canal: Panama"

s2 = s.lower()
test = ""

print(s2)

for i in range (len(s)) :
    l = ""
    l = s2[i]
    if (l.isalnum() == True) :
        test += s2[i]
    else :
        continue

x = ""

for i in range (len(test)-1, -1, -1) :
    x += test[i]

if (x == test) :
    print("Is palindrome")

print(test)
print(x)
