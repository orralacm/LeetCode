#You are given a sorted unique integer array nums.
#Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

nums = [0,1,2,4,5,7]

class Object :
    def summaryRanges(self, nums):
        if not nums:
            print([])
        res, i, start = [], 0, 0
        while i < len(nums)-1:
            if nums[i]+1 != nums[i+1]:
                res.append(self.printRange(nums[start], nums[i]))
                start = i+1
            i += 1
        res.append(self.printRange(nums[start], nums[i]))
        print(res)

    def printRange(self, l, r):
        if l == r:
            return str(l)
        else:
            return str(l) + "->" + str(r)
    
    summaryRanges(self, nums)

