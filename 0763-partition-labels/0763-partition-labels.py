class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dicts = {char: index for index , char in  enumerate(s)}
        max_value , min_value , result  = 0  ,0 , []

        for idx , char in enumerate(s):
            max_value = max(max_value , dicts[char])

            if max_value == idx:
                result.append(idx - min_value + 1)
                min_value = idx + 1
        
        return result 

        