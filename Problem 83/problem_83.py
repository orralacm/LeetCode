nums = [1,1,2, 3, 3]

for i in range (len(nums)-2) :
    j = i + 1
    print(nums)
    print(len(nums))
    if (nums[i] == nums[j]) :
        nums.pop(j)
        print("Pop")
        print(len(nums))
    else :
        print("Continue")
        print(len(nums))
        continue
    print(nums)
print(nums)