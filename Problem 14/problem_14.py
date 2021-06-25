
strs = ["flower", "flow", "flight"]
strs.sort(key=len)
output = ""
base = strs[0]

print(strs)

if (strs == 0) :
    print ("")

for i in range (1, len(strs)) :
    print(base)
    word = strs[i]
    print(word)
    for j in range (0, len(base)) :

        if (output == "") :
            if (word[j] == base[j]) :
                output += word[j]
        elif (output[j] == word[j]) :
            output += word[j]

print(output)
    