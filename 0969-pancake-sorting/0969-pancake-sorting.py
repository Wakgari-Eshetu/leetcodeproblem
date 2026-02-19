class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        for i in range(len(arr)-1 , 0 ,-1):
            mx = max(arr[:i+1])
            index_mx = arr.index(mx)

            if index_mx == i:
                continue
            
            if index_mx != 0:
                arr[:index_mx+1] = reversed(arr[:index_mx+1])
                result.append(index_mx+1)
            arr[:i+1] = reversed(arr[:i+1])
            result.append(i+1)
        
        return result 
        