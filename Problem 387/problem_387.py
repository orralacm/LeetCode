#Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

s = "aabbcc"

start, end = 0, len(s)

while start < end :
    if s.count(s[start]) == 1 :
        print(s.index(s[start]))
        break
    elif s.count(s[start]) > 1 :
        start += 1
    if start == end :
        print("-1")
