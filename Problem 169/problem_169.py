#Given an array nums of size n, return the majority element.

nums = [2,2,1,1,1,2,2]
nums.sort()
n = 0
output = 0

for i in range (len(nums)) :
    if (nums.count(nums[i]) > n) :
        n = nums.count(nums[i])
        print(n)
        output = nums[i]
    else :
        continue

print(f"The majority element is: {output}")
