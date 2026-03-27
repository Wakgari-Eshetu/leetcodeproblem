class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count , prefix_sum = 0 , 0
        dict_count = {0:1} 

        for num in nums:
            prefix_sum += num
            rem = prefix_sum % k
            if rem < 0:
                rem += k 
            
            if rem in dict_count:
                count += dict_count[rem]
            
            dict_count[rem] = dict_count.get(rem , 0) + 1
        return count 

            



        