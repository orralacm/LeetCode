
s = "aabbcc"

d = {}
seen = set()
for idx, c in enumerate(s):
    if c not in seen:
        d[c] = idx
        seen.add(c)
    elif c in d:
        del d[c]

print(min(d.values())) if d else print(-1)

