def merge(nums1, nums2,m,n):
    i = 0
    for j,num in enumerate(nums1[m:]):
        if num == 0:
            nums1[m+j] = nums2[i]
            i += 1
            print(nums1)
    nums1.sort()
    print(nums1)

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
merge(nums1,nums2,3,3)
