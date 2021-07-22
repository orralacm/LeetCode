digits = [1,2,3]
integer = 0
for i in range (len(digits)) :
    integer *= 10
    integer += digits[i]
    print(f"value of integer: {integer}")
integer += 1
print(f"integer plus one: {integer}")
digits[-1] += 1
print(f"the final array: {digits}")