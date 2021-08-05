numbers = [2,3,4]
target = 6

for i in range (0, len(numbers)) :
    print(i)
    for j in range (1, len(numbers)) :
        print(j)
        if ((numbers[i] + numbers[j]) == target) :
            print(f"[{i}], [{j}]")
            break
