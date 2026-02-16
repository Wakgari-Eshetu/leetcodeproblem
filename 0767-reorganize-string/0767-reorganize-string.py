class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_freq = max(count.values())
        if max_freq > (len(s)+1)//2:
            return ""
        result = [None] * len(s)
        curr_index = 0
        for char, freq in count.most_common():
            while freq > 0:
                result[curr_index] = char
                freq -= 1
                curr_index += 2
                if curr_index >= len(s):
                    curr_index = 1
        
        return ''.join(result)
        

            
            
            
        