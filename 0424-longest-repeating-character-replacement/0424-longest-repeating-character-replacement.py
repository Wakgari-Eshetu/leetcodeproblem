class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = Counter()
        mostfreq , left = 0,0
        for right , char in enumerate(s):
            count[char] += 1
            mostfreq = max(mostfreq , count[char])

            if right-left + 1 - mostfreq > k:
                count[s[left]] -= 1
                left += 1

        return len(s) - left 
        