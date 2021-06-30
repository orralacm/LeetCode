
nums = [1,3,5,6]
target = 0
a = 0

print(nums)
print(target)

if (nums[len(nums)-1] < target) :
    print(f"no iteration, target is higher than nums[max], so output is:  {len(nums)}")
else :
    while (nums[a] < target) and (a < len(nums)-1) :
        if (nums[a] != target) :
            print(f"iteration, value of nums[a]: {nums[a]}")
            a += 1
        elif (nums[a] == target) :
            print(f"elif, output is value of a: {a}")
            a += 1
    else :
        print(f"else, output is value of a: {a}")


#for i in range(len(nums)-1) :
   # if (nums[a] == target) :
        #print(nums.index(target))
        #a += 1
        #break
    #else :
        #print(nums[a])
        #a += 1