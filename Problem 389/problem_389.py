#You are given two strings s and t.
#String t is generated by random shuffling string s and then add one more letter at a random position.
#Return the letter that was added to t.

s = "abcd"
t = "abcde"

dic = {}
print(dic)

for ch in s:
    dic[ch] = dic.get(ch, 0) + 1
    print(dic)
for ch in t:
    if dic.get(ch, 0) == 0:
        print(ch)
    else:
        dic[ch] -= 1
