#Given a string s, reverse only all the vowels in the string and return it.
#The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

s = "leetcode"

vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

start, end = 0, len(s)-1

s = list(s)

while start < end:
    if s[start] in vowels and s[end] in vowels:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    elif s[start] in vowels:
        end -= 1
    elif s[end] in vowels:
        start += 1 
    else:
        start += 1
        end -= 1
print(s)