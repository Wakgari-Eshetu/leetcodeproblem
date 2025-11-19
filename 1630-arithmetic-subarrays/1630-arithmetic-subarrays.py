class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i in range(len(l)):
            result =nums[l[i]:r[i]+1]
            result = sorted(result)
            if len(result)<2:
                ans.append(False)
                continue
            dif = []
            for j in range(len(result)-1):
                dif.append(result[j+1]-result[j])
            
            check = True
            for d in dif:
                if d!=dif[0]:
                    check=False
                    break
            ans.append(check)
        return ans

        