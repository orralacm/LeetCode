
l1 = [1,2,4]
l2 = [1,3,4]

for i in range (0, len(l2)-1) :
    x = l2.pop(i)
    l1.append(x)

l1.sort()

print(l1)