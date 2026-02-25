class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = Counter()
        left , max_value = 0 ,0
        for right , char in enumerate(s):
            count[char] += 1

            while count[char] > 1:
                count[s[left]] -= 1
                left += 1
            
            max_value = max(max_value , right - left + 1)
        
        return max_value 

        

        