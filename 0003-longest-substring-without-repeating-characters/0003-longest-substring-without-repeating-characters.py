class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = Counter()
        longest_substring , left = 0,0
        for right in range(len(s)):
            count[s[right]] += 1
            while count[s[right]] > 1:
                count[s[left]] -= 1
                left += 1
            
            longest_substring = max(longest_substring , right - left + 1)
        
        return longest_substring
