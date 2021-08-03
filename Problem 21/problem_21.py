
l1 = [1,2,4, 6, 7]
l2 = [1,3,4, 6, 7]

for i in range (len(l2)-1, -1, -1) :
    print(i)
    x = l2.pop(i)
    print(x)
    l1.append(x)

l1.sort()

print(l1)