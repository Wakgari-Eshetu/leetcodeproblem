class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for char in count:
            if count[char]==1:
                for i in range(len(s)):
                    if char == s[i]:
                        return i
        return -1
        