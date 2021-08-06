numbers = [2,3,4]
target = 6
output = []

for i in range (0, len(numbers)) :
    print(i)
    for j in range (1, len(numbers)) :
        print(j)
        if ((numbers[i] + numbers[j]) == target and (numbers[i] != numbers[j])) :
            output = [i+1, j+1]
            print(output)
            break
    if (output) :
        break
