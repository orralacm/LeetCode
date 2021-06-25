
nums = [0,1,2,2,3,0,4,2]
val = 2
x = 0

while x < len(nums) :

    if (nums[x] == val) :

        nums.pop(x)
        nums.append("")
        
        print("if")

    else :

        x += 1        
        print("else")

    print(nums)
    print("end cycle")

print(nums)
