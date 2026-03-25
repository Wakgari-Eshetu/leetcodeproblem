class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #[1, 2,3,4] [1, 2 ] , [1,3] 
        list_of_numbers = []
        for x in range(1, n+1):
            list_of_numbers.append(x)
        
        ans = []
        for c in combinations(list_of_numbers , k):
            ans.append(c)
        
        return ans
              