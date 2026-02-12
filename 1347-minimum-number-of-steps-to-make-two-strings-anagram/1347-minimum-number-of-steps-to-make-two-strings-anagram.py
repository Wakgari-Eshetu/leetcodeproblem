class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count1 = Counter(t)
        count2 = Counter(s)
        
        result = 0
        for char in count1:
            if count1[char] > count2[char]:
                result += count1[char] - count2[char]
        
        return result 


        