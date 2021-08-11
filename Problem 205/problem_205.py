#Given two strings s and t, determine if they are isomorphic.

s = "paper"
t = "title"

ns = len(s)
nt = len(t)

if ns != nt:
    print("No isomorphic")
    
h = {}
mt = {}
for i in range(ns):
    if s[i] not in h:
        if t[i] not in mt:
            h[s[i]] = t[i]
            mt[t[i]] = s[i]
        else:
            print("No isomorphic")
    elif h[s[i]] != t[i]:
        print("No isomorphic")
    
    else :
        print("Isomorphic")