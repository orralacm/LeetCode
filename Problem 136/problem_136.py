nums = [4,1,2,1,2]

for i in range (len(nums)) :
    n = nums[i]
    if (nums.count(n) < 2) :
        print(n)
    else :
        continue
