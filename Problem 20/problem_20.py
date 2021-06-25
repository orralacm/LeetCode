isValid = "([)]"

for i in range(0, len(isValid)) :
    j = i + 1
    if isValid[i] == "(" :
        if isValid[j] == ")" :
            i += 1
        else :
            break

    elif isValid[i] == "[" :
        if isValid[j] == "]" :
            i += 1
        else :
            break
   
    elif isValid[i] == "{" :
        if isValid[j] == "}" :
            i += 1
        else :
            break

print(i==len(isValid)-1)
