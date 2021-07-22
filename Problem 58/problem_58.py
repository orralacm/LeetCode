
s = "Hello World"
word = ""

if (s[-1] == " ") :
    word = ""
    print(0)
else :
    for i in range (1, len(s) + 1) :
        print(f"value of i: {i}")
        r = (-1) * i
        print(f"value of r: {r}")
        if (s[r] == " ") :
            break
        word += s[r]
        print(f"word is: {word}")
    l = len(word)
    print(f"lenght of last word is: {l}")
