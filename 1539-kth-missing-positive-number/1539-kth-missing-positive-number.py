class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        mis, cur , i = 0,1,0
        while True:
            if i<len(arr) and arr[i] == cur:
                i+=1
            else:
                mis += 1
                if mis == k:
                    return cur
            cur += 1

                
        
        


        