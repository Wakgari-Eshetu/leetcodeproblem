class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_2 = Counter(magazine)

        for char in ransomNote:
            count_2[char] -= 1
            
            if count_2[char] < 0:
                return False
        
        return True 

        