class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list1 = s.split()
        if len(pattern) != len(list1):
            return False
        list2 = [x for  x in pattern ]
        dict1 = {}
        dict2 = {}
        for char_pattern , char_s in zip(list2, list1):
            if char_pattern in dict1 and dict1[char_pattern] != char_s:
                return False 
            
            if char_s in dict2 and dict2[char_s] != char_pattern:
                return False 
            
            dict1[char_pattern] = char_s
            dict2[char_s] = char_pattern
        
        return True
        