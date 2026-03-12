class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter()
        count1 = Counter(s1)
        left = 0
        for right in range(len(s2)):
            count[s2[right]] += 1
             
            while  right - left + 1 > len(s1):
                count[s2[left]] -= 1
                if count[s2[left]] == 0:
                    del count[s2[left]]
                left += 1
            if count == count1:
                return True
        return False 

        