
nums = [0,0,1,1,1,2,2,3,3,4]

for i in range (0, len(nums)-1) :
    j = i + 1
    print(nums)
    print(len(nums))
    if (nums[i] == nums[i]) :
        nums.pop(i)
        nums.append("")
        print("Pop")
        print(len(nums))
    else :
        print("Continue")
        print(len(nums))
        continue
    print(nums)
print(nums)
