
strs = ["flower", "flow", "flight"]
strs.sort(key=len)
output = ""
base = strs[0]
l = len(base)
letter = ""

print(strs)

if (strs == 0 or len(strs) == 0) :
    print ("")
if (len(strs) == 1) :
    print (strs[0])

for i in range (len(strs[0])) :
    letter = base[i]
    
    a = 0
    for j in range (1, len(strs)) :
        word = strs[j]
        if (letter == word[i]) :
            a += 1
    if (a == len(strs)-1) :
        output += base[i]
        print(output)




