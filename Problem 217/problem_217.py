#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

nums = [1,1,1,3,3,4,3,2,4,2]
a = 0

for i in range (len(nums)) :
    if (nums.count(nums[i]) > 1) :
        print("True")
        break
    else :
        a = 1
        continue
if (a > 0) :
    print("False")
