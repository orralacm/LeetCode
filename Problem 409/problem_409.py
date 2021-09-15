#Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
#Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

s = "abccccdd"

dic = {}

for ch in s:
    dic[ch] = dic.get(ch, 0) + 1
    print(dic)
    print(ch)

a, b = 0, 0

for value in dic.values() :
    if value % 2 == 0 :
        a += value
    else :
        b += value - 1
        a = 1
print(b + a)
