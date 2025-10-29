class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    return nums1[i]
                elif nums2[j] >nums1[i]:
                    break        
        return -1
                    
        
        