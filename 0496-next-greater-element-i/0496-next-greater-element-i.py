class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans  =[]

        for i in range(len(nums1)):
            val = -1
            for j in range(len(nums2)-1):
                if nums1[i] == nums2[j]:
                    for k in range(j,len(nums2)):
                        if nums2[j]<nums2[k]:
                            val=nums2[k]
                            break

            ans.append(val)
        return ans  

        