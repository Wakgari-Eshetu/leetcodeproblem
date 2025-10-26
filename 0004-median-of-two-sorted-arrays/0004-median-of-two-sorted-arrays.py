class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for char in nums2:
            nums1.append(char)
        n=len(nums1)
        nums1=sorted(nums1)
        if n%2==0:
            m=n//2
            return (nums1[m]+nums1[m-1])/2
        else:
            return nums1[(n-1)//2]

        