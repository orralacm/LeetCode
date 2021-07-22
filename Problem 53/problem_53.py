
nums = [5,4,-1,7,8]

sum = 0

if (len(nums) == 1) :
    print(nums[a])
else :
    for i in range (len(nums)) :
        print(f"sum is: {sum}")
        sumj = 0
        for j in range (i, len(nums)) :
            sumj += nums[j]
            print(f"value of sumj: {sumj}")
            if (sumj > sum) :
                sum = sumj
    print(f"the highest sum of a contiguous subarray is: {sum}")

