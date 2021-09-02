#Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

nums1=set(nums1)
nums2=set(nums2)

print(list(nums1&nums2))
