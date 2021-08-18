
s = "anagram"
t = "nagaram"

maps = {}
mapt = {}
for c in s:
    maps[c] = maps.get(c,0)+1
    print(maps)
for c in t:
    mapt[c] = mapt.get(c,0)+1
    print(mapt)
    
print(maps == mapt)