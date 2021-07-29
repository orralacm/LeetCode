
strs = ["flower", "flow", "flight"]
strs.sort(key=len)
output = ""
base = strs[0]
l = len(base)

print(strs)

if (strs == 0) :
    print ("")

#for i in range (0, len(base)) :
    #for j in range (0, len(strs)-1) :
        


for i in range (1, len(strs)-1) :
    print(base)
    word = strs[i]
    print(word)
    for j in range (0, len(base)) :
        if (base[j] == word[j]) :
            output += base[j]
        else :
            break
        
        print(output)
    
    if (output == "") :
        break

print(output)

