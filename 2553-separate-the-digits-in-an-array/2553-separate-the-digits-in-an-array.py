class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            tostring = str(nums[i])
            for j in range(len(tostring)):
                result.append(int(tostring[j]))
        
        return result 
        