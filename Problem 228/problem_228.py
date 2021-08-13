#You are given a sorted unique integer array nums.
#Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

nums = [0,1,2,4,5,7]
output = []
i = 0

while (i < len(nums)) :
    if (nums[i+1] == (nums[i]+1)) :
        a = nums[i]
        if ()
        output += [f"{i} -> {i+1}"]
        print(output)
        i += 1

