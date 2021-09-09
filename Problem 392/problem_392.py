#Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

s = "abc"
t = "ahbgdc"
tt = list(t)

dic = {}

for ch in s :
    dic[ch] = dic.get(ch, 0) + 1
    print(dic)
i = 0
for ch in t :
    if t[i] not in dic :
        tt.pop(i)
    i += 1
    print(dic)
