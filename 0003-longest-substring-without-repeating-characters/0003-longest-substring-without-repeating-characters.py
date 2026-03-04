class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = Counter()
        left , longest_value  = 0 , 0
        for right in range(len(s)):
            count[s[right]] += 1
            while count[s[right]] > 1:
                count[s[left]] -= 1
                left += 1
            longest_value = max(longest_value , right - left + 1 )
        
        return longest_value


        