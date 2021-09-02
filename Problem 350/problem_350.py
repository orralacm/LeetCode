#Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

nums1 = [1,2,2,1]
nums2 = [2,2]

nums1, nums2 = sorted(nums1), sorted(nums2)

print(nums1)
print(nums2)

pt1 = pt2 = 0
res = []

while True:
    try:
        if nums1[pt1] > nums2[pt2] :
            pt2 += 1
        elif nums1[pt1] < nums2[pt2] :
            pt1 += 1
        else:
            res.append(nums1[pt1])
            pt1 += 1
            pt2 += 1
    except IndexError :
        break

print(res)
