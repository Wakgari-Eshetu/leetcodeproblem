class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagram = []
        count_p = Counter(p)
        n = len(p)
        left = 0
        for right in range(n-1 ,len(s)):
            count_s = Counter(s[left:right+1])
            if count_s == count_p:
                anagram.append(left)
            left += 1


        return anagram 
        
        