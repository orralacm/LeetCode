
s = "CDLXIV"
integer = 0
intarray = []
for i in range (0, len(s)):
    j = i + 1
    roman = ""
    num = 0        
    if (s[i] == "I"):
        if (s[j] == "V"):
            num = 4
            roman = s[i] + s[j]
            i += 1
        elif (s[j] == "X"):
            num = 9
            roman = s[i] + s[j]
            i += 1
        else:
            num = 1
            roman = s[i]
    
    if (s[i] == "X"):
        if (s[j] == "L"):
            num = 40
            roman = s[i] + s[j]
            i += 1
        elif (s[j] == "C"):
            num = 90
            roman = s[i] + s[j]
            i += 1
        else:
            num = 10
            roman = s[i]
    
    if (s[i] == "C"):
        if (s[j] == "D"):
            num = 400
            roman = s[i] + s[j]
            i += 1
        elif (s[j] == "M"):
            num = 900
            roman = s[i] + s[j]
            i += 1
        else:
            num = 1000
            roman = s[i]
    
    def switch_demo (roman):
        I: num = 1,
        IV: num = 4,
        IX: num = 9,
        V: num = 5,
        X: num = 10,
        XL: num = 40,
        XC: num = 90,
        L: num = 50,
        C: num = 100,
        CD: num = 400,
        CM: num = 900,
        D: num = 500,
        M: num = 1000,
    
    integer += num
print(integer)