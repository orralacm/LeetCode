#Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

nums = [3,0,1]

nums.sort()

for i in range (len(nums)-1) :
    if (nums[i+1] - nums[i] != 1) :
        print(f"Missing number is: {nums[i]}")
    else :
        continue
