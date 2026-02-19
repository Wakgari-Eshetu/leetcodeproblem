class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(n) for n in nums]
        def custom_compare(x,y):
            if x+y < y+x:
                return 1
            else:
                return -1
        
        nums.sort(key=cmp_to_key(custom_compare))

        if nums[0] == "0":
            return "0"
        else:
            return "".join(nums)
                        
        